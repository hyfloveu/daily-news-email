# 📧 AI 每日科技新闻邮件助手 (AI Daily News Email Bot)

这是一个基于 Python 和 GitHub Actions 的自动化开源项目。它可以每天定时抓取主流科技媒体（如 36氪、少数派、爱范儿）的 RSS 源，利用大语言模型（LLM）进行智能筛选和摘要总结，并自动发送一封排版精美的 HTML 邮件到你的邮箱。

## ✨ 项目亮点

- **零服务器成本**：完全依托于 GitHub Actions 运行，每月免费额度足够使用。
- **AI Agent 加持**：接入 DeepSeek / 智谱等大模型，自动挑选最有价值的新闻，并生成 150-250 字的总摘要。
- **高度安全**：所有敏感信息（API Key、邮箱授权码）均通过 GitHub Secrets 注入，代码开源绝无泄露风险。
- **开箱即用**：自动识别 QQ/163/Gmail 等常见邮箱的 SMTP 服务器，无需繁琐配置。

## 🚀 如何拥有你自己的每日邮件？

如果你想 Fork 这个项目并让它每天为你服务，只需以下 3 步：

### 1. Fork 本仓库
点击页面右上角的 `Fork` 按钮，将代码复制到你的个人账户。

### 2. 配置环境变量 (Secrets)
在你的仓库页面，点击 `Settings` -> `Secrets and variables` -> `Actions`，点击 `New repository secret`，依次添加以下 5 个变量：

| 变量名 (Name) | 描述 (Secret) | 示例 |
| :--- | :--- | :--- |
| `LLM_API_KEY` | 你的大模型 API Key | `sk-xxxxxxxxxxx` |
| `LLM_BASE_URL` | 模型接口地址 | `https://api.deepseek.com/v1` |
| `EMAIL_USER` | 发件人邮箱 | `your_email@qq.com` |
| `EMAIL_PASS` | 邮箱 SMTP 授权码 | `abcdefghijklmnop` |
| `TO_EMAIL` | 收件人邮箱 | `receiver@163.com` |

*(注：请确保已在你的发件邮箱网页端开启了 SMTP 服务，获取授权码，而不是登录密码。)*
如果发件邮箱和收件邮箱一样，那你的每日新闻可能会被丢进“垃圾邮箱”

### 3. 开启定时任务
打开 `.github/workflows/daily.yml` 文件，找到以下两行代码，取消前面的 `#` 注释：
```yaml
on:
  schedule:
    - cron: '0 0 * * *' # 每天 UTC 0点 (北京时间早上 8点) 运行
