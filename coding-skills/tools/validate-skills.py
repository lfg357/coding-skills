#!/usr/bin/env python3
"""校验 Skill 文件格式合规性。"""

import yaml
import sys
import pathlib
from typing import List, Dict

REQUIRED_FIELDS = ["name", "description"]
SKILLS_DIR = pathlib.Path("skills")


def validate_skill(path: pathlib.Path) -> List[str]:
    """校验单个 SKILL.md 文件。"""
    errors = []

    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        return [f"{path}: 读取失败 - {e}"]

    # 检查 frontmatter
    if not content.startswith("---"):
        return [f"{path}: 缺少 YAML frontmatter"]

    end = content.find("---", 3)
    if end == -1:
        return [f"{path}: frontmatter 未闭合"]

    try:
        fm = yaml.safe_load(content[3:end])
    except yaml.YAMLError as e:
        return [f"{path}: frontmatter YAML 解析失败 - {e}"]

    if fm is None:
        return [f"{path}: frontmatter 为空"]

    for field in REQUIRED_FIELDS:
        if field not in fm:
            errors.append(f"{path}: frontmatter 缺少必填字段 '{field}'")

    # 检查正文
    body = content[end+3:].strip()
    if len(body) < 100:
        errors.append(f"{path}: 正文内容过少（< 100 字符）")

    return errors


def main():
    if not SKILLS_DIR.exists():
        print(f"❌ 目录不存在: {SKILLS_DIR}")
        sys.exit(1)

    all_errors = {}
    skill_count = 0

    for skill_dir in SKILLS_DIR.iterdir():
        if not skill_dir.is_dir():
            continue

        skill_md = skill_dir / "SKILL.md"
        if not skill_md.exists():
            all_errors[str(skill_dir)] = ["缺少 SKILL.md"]
            continue

        skill_count += 1
        errors = validate_skill(skill_md)
        if errors:
            all_errors[str(skill_dir)] = errors

    print(f"🔍 发现 {skill_count} 个技能\n")

    if not all_errors:
        print("✅ 所有 Skill 格式合规！")
        sys.exit(0)

    print(f"❌ 发现 {len(all_errors)} 个问题：\n")
    for skill_path, errors in all_errors.items():
        print(f"📁 {skill_path}")
        for err in errors:
            print(f"   - {err}")
        print()

    sys.exit(1)


if __name__ == "__main__":
    main()
