#!/usr/bin/env python3
"""Небольшое приложение для практики Git и Docker."""

from datetime import datetime, timezone


def main() -> None:
    print("Привет! Это учебный проект по Git и Docker.")
    print("Автор: Кузьменко Валентин Сергеевич")
    print("Группа: БИ-3-24-02")
    print(f"Время UTC: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')}")


if __name__ == "__main__":
    main()
