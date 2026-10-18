"""Read JUnit results and distinguish repeat failures from flaky outcomes."""
from runtime import *

import xml.etree.ElementTree as ET
def process(data):
    reports=records(data,"reports")
    unique(reports)
    grouped={}
    totals={k:0 for k in ("passed","failed","error","skipped")}
    for report in reports:
        xml=text(report.get("xml"),"xml")
        if "<!DOCTYPE" in xml.upper() or "<!ENTITY" in xml.upper(): raise ValueError("DTD/entity declarations are not supported")
        try: root=ET.fromstring(xml)
        except ET.ParseError as exc: raise ValueError("invalid JUnit XML") from exc
        local=lambda tag:tag.rsplit("}",1)[-1]
        if local(root.tag) not in ("testsuite","testsuites"): raise ValueError("expected JUnit testsuite(s)")
        for case in root.iter():
            if local(case.tag)!="testcase": continue
            name=text(case.get("name"),"test name")
            key=case.get("classname","")+"::"+name
            duration=float(case.get("time","0"))
            number(duration,"test duration",0)
            children={local(c.tag):c for c in case}
            kind="error" if "error" in children else "failed" if "failure" in children else "skipped" if "skipped" in children else "passed"
            child=children.get({"error":"error","failed":"failure","skipped":"skipped"}.get(kind,""))
            message="" if child is None else child.get("message","")+" "+(child.text or "")
            grouped.setdefault(key,[]).append({"report":report["id"],"outcome":kind,"seconds":duration,"message":message.strip()})
            totals[kind]+=1
    tests=[]
    for key,observations in sorted(grouped.items()):
        outcomes={r["outcome"] for r in observations}
        tests.append({"test":key,"observations":observations,"mixed_outcomes":"passed" in outcomes and bool(outcomes & {"failed","error"})})
    return {"totals":totals,"tests":tests}

if __name__ == "__main__":
    sys.exit(main(process, "Read JUnit results and distinguish repeat failures from flaky outcomes."))
