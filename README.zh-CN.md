# Test Failure Triage · 测试失败归类

[English](README.md) | 简体中文

把多份 JUnit 报告放在一起，查看哪些测试持续失败、哪些在不同运行中结果不一致。每次观察都保留报告来源、耗时和失败消息，方便继续查原因。

[下载 v0.2.1](https://github.com/KarmenLoop/skill-test-failure-triage/releases/tag/v0.2.1) · [完整教程](docs/tutorial.zh-CN.md) · [输入参考](docs/input.zh-CN.md) · [反馈问题](https://github.com/KarmenLoop/skill-test-failure-triage/issues)

## 能做什么

save::roundtrip 一次失败、一次通过；totals 统计两次观察，mixed_outcomes 为 true。

结果不一致只是调查线索，不能直接证明测试不稳定。工具只读取报告 XML，不会运行或修复测试。

![测试失败归类 0.2.1 版本样例的真实 JSON 输出](docs/images/example-output-v0.2.1.svg)

*图片来自 v0.2.1 的真实本地输出，采用英文键名；[完整结果](examples/expected.json) · [图片来源记录](docs/images/provenance.json)。*

## 开始使用

在发行页下载 `karmen-test-failure-triage-v0.2.1.zip` 与对应 `.sha256` 文件，核对哈希后解压。在解压目录中使用 Python 3.9 或更新版本：

```sh
python3 scripts/run.py --version
python3 scripts/run.py --input examples/input.json
```

预期版本：`karmen-test-failure-triage 0.2.1`。save::roundtrip 一次失败、一次通过；totals 统计两次观察，mixed_outcomes 为 true。

如果宿主读取 `~/.agents/skills`，可安装完整技能：

```sh
python3 install.py --host agents
```

目标目录已存在时安装器会拒绝覆盖。宿主发现和调用方式可能不同，见[安装与实践教程](docs/tutorial.zh-CN.md)。不使用 AI 宿主也能直接运行本地工具。

## 用于自己的任务

每份报告使用唯一 ID，并提供 XML 文本。以 testcase 条目为依据；不接受 DTD 或实体声明。

加入已知版本的第三份报告，比较失败消息。调查结果不一致时，把提交、环境和命令与报告一起保存。

准备新输入前可查看[字段约定](docs/input.zh-CN.md)。工具只依赖 Python 标准库，本身不需要模型账号、API 密钥或网络。使用 AI 宿主时，宿主有自己的数据与权限设置。

## 常见问题

**出现 mixed_outcomes 就能忽略失败吗？** 不能。应检查版本与环境差异，按计划复现，并在改变测试状态前修复原因。

**结果保存在哪里？** 默认向终端输出 JSON；使用 `--output` 时只创建新文件，已有输出文件会保留。工具只读取提交的记录和输入约定中明确列出的本地路径。

## 文档与支持

- [下载、安装、配置、练习、升级与卸载](docs/tutorial.zh-CN.md)
- [输入输出约定](docs/input.zh-CN.md)与[兼容性说明](docs/COMPATIBILITY.md)（英文参考）
- [更新记录](CHANGELOG.md)、[参与贡献](CONTRIBUTING.md)、[支持](SUPPORT.md)和[安全反馈](SECURITY.md)

## 许可证

[MIT](LICENSE)。再分发时保留许可证和[声明](NOTICE.md)。由 [KarmenLoop](https://karmenloop.com) 维护。
