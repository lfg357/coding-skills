# Claude Code 集成指南

## 使用方式

1. 启动 Claude Code 时加载技能：

```bash
claude --system-prompt skills/universal-karpathy-coding-guidelines/SKILL.md
```

2. 在对话中引用特定技能：

```
> 参考 skills/flask-web-dev/SKILL.md，帮我设计 API 路由
```

## 全局配置

将以下内容添加到 `~/.claude/config.toml`：

```toml
[system_prompts]
karpathy = "skills/universal-karpathy-coding-guidelines/SKILL.md"
flask = "skills/flask-web-dev/SKILL.md"
frontend = "skills/frontend-compatibility/SKILL.md"
```
