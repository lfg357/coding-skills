# Trae 集成指南

## 方式一：通过 `npx skills` 安装（推荐）

```bash
# 安装所有技能
npx skills add YOUR_USERNAME/trae-coding-skills --all

# 安装特定技能
npx skills add YOUR_USERNAME/trae-coding-skills --skill universal-karpathy-coding-guidelines

# 全局安装
npx skills add YOUR_USERNAME/trae-coding-skills --all --global
```

## 方式二：手动导入

1. 打开 **Trae → 设置 → 规则和技能 → 技能 → 创建**
2. 选择 `skills/xxx/SKILL.md` 文件或 ZIP
3. Trae 自动解析 frontmatter 和正文

## 方式三：项目级规则

将技能复制到项目目录：

```bash
mkdir -p .trae/skills
cp -r skills/* .trae/skills/
```

Trae 会自动加载 `.trae/skills/` 下的所有 SKILL.md。

## 技能协同

Trae 会自动根据文件类型和上下文激活对应技能：

| 场景 | 自动激活技能 |
|------|------------|
| 编写 Python/Flask 代码 | `universal-karpathy-coding-guidelines` + `flask-web-dev` |
| 修改 HTML/CSS/JS | `universal-karpathy-coding-guidelines` + `frontend-compatibility` |
| 全栈开发（前后端） | `universal-karpathy-coding-guidelines` + `flask-web-dev` + `frontend-compatibility` + `hybrid-python-web` |
| Bug 修复/代码审查 | `universal-karpathy-coding-guidelines`（主技能） |

## 设置片段

将以下内容添加到 Trae System Prompt：

```markdown
你是遵循 Trae Coding Skills 规范的 AI 编程助手。

核心原则：
1. 绝不擅自假设，只基于已有代码和明确需求
2. 拒绝过度设计，不为"未来可能"添加抽象层
3. 每段代码必须解决具体问题，禁止无目标编码
4. 修改前说明理由，修改后说明影响范围

技能激活规则：
- 代码编写/实现 → karpathy-style（清晰显式）+ minimal-coding（最小可行）
- 代码审查 → code-review（P0/P1/P2 分级）
- Bug 修复 → bug-fix（根因分析）+ test-driven（回归测试）
- 性能优化 → optimization（需基准数据）
- 纯概念问答 → 不输出代码，仅解释概念
```
