import os
from pathlib import Path

from dotenv import load_dotenv


TEST_HTML = """
<h2>邮件配置测试</h2>
<p>如果你收到这封邮件，说明本地 SMTP 配置可以正常发送 HTML 邮件。</p>
<p>这封邮件由 <strong>test.py</strong> 发送。</p>
"""


def main() -> int:
    env_path = Path(__file__).resolve().parent / ".env"
    if not env_path.exists():
        print(f"未找到环境变量文件：{env_path}")
        return 1

    load_dotenv(dotenv_path=env_path, override=True)
    os.environ.setdefault("MAIL_SUBJECT", "科技新闻邮件配置测试")

    try:
        from main import send_email

        send_email(TEST_HTML)
        print("测试邮件发送成功。")
        return 0
    except Exception as exc:
        print(f"测试邮件发送失败：{exc}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
