# Contributing Guide

感谢你对 Trae Coding Skills 的贡献！

## 提交规范

### 新增技能

1. 在 `skills/` 下创建 `{skill-name}/` 目录
2. 目录内必须包含 `SKILL.md`（核心文件）
3. `SKILL.md` 必须包含 YAML frontmatter：
   ```yaml
   ---
   name: skill-name
   description: "清晰描述技能用途和触发条件"
   version: "1.0.0"
   author: "Your Name"
   license: MIT
   ---
   ```
4. 正文使用 Markdown 格式，包含：
   - 触发条件（何时使用）
   - 核心规则/原则
   - 代码示例（Before/After）
   - 禁止行为（❌）
   - 推荐做法（✅）

### 修改现有技能

1. 遵循 Semver 版本规范：
   - 新增规则 → Minor 版本（1.0.0 → 1.1.0）
   - 修复描述/示例 → Patch 版本（1.0.0 → 1.0.1）
   - 移除/重命名规则 → Major 版本（1.0.0 → 2.0.0）
2. 更新 `SKILL.md` 中的 `version` 字段
3. 在 CHANGELOG 中说明变更

### 本地校验

```bash
python tools/validate-skills.py
```

所有 `SKILL.md` 必须通过校验后才能提交 PR。

## 技能质量标准

- **触发条件清晰**：AI 能准确判断是否该使用此技能
- **规则可执行**：每条规则都能转化为具体的代码行为
- **示例真实**：Before/After 示例必须是真实可运行的代码
- **无矛盾**：技能内部规则不冲突，多个技能之间不冲突
