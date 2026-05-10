# Cursor 集成指南

## 使用 .cursorrules

在项目根目录创建 `.cursorrules` 文件：

```markdown
# Trae Coding Skills - Cursor 适配版

## 核心原则
1. 绝不擅自假设，只基于已有代码和明确需求
2. 拒绝过度设计，不为"未来可能"添加抽象层
3. 每段代码必须解决具体问题，禁止无目标编码
4. 修改前说明理由，修改后说明影响范围

## 技能激活
- Python/Flask 项目 → 参考 skills/flask-web-dev/SKILL.md
- 前端开发 → 参考 skills/frontend-compatibility/SKILL.md
- 全栈开发 → 参考 skills/hybrid-python-web/SKILL.md
- 代码审查 → 按 P0/P1/P2 分级输出

## 约束
- 纯概念问答时不输出代码
- 优先使用标准库，最小化依赖
- 所有修改必须有明确理由
```

## 使用 @ 引用

在 Cursor Chat 中使用 `@` 引用技能文件：

```
@skills/universal-karpathy-coding-guidelines/SKILL.md
帮我 review 这段代码
```
