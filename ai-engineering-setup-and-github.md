# AI Engineering 开发环境搭建与 GitHub 同步记录

> 本文记录从零搭建 `ai-engineering` Python 项目、配置开发环境、使用 Git
> 进行版本管理，并同步到 GitHub 的完整过程。
>
> GitHub 仓库：`https://github.com/xuxuxu121/ai-engineering`

------------------------------------------------------------------------

## 1. 开发环境

  工具          版本                   状态
  ------------- ---------------------- ------
  Git           2.54.0.windows.1       ✅
  VS Code       1.130.0                ✅
  Python        3.14.5                 ✅
  uv            0.12.5                 ✅
  Python 扩展   Microsoft Python       ✅
  Pylance       Microsoft Pylance      ✅
  Ruff          Astral Software Ruff   ✅
  Error Lens    Error Lens             ✅
  GitLens       GitLens                ✅

------------------------------------------------------------------------

## 2. 检查 Git

在 CMD 中：

``` cmd
git --version
```

成功结果：

``` text
git version 2.54.0.windows.1
```

说明 Git 安装成功。

------------------------------------------------------------------------

## 3. 检查 VS Code

``` cmd
code --version
```

成功显示：

``` text
1.130.0
...
x64
```

说明 VS Code 安装成功，并且 `code` 命令可以直接使用。

------------------------------------------------------------------------

## 4. 检查 Python

``` cmd
python --version
```

成功结果：

``` text
Python 3.14.5
```

说明 Python 已经安装。

------------------------------------------------------------------------

## 5. 安装 uv

第一次检查：

``` cmd
uv --version
```

如果提示：

``` text
'uv' 不是内部或外部命令，也不是可运行的程序
```

说明 uv 尚未安装。

Windows 安装命令：

``` powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

安装完成后：

``` text
everything's installed!

installing to C:\Users\29157\.local\bin
  uv.exe
  uvx.exe
  uvw.exe
```

如果当前 CMD 没有自动刷新 PATH，可以临时执行：

``` cmd
set Path=C:\Users\29157\.local\bin;%Path%
```

然后检查：

``` cmd
uv --version
```

成功结果：

``` text
uv 0.12.5 (210d1f678 2026-08-14 x86_64-pc-windows-msvc)
```

------------------------------------------------------------------------

## 6. 创建 AI Engineering 项目目录

进入用户目录：

``` cmd
cd C:\Users\29157
```

创建项目：

``` cmd
mkdir ai-engineering
```

进入项目：

``` cmd
cd ai-engineering
```

检查当前位置：

``` cmd
cd
```

结果：

``` text
C:\Users\29157\ai-engineering
```

------------------------------------------------------------------------

## 7. 使用 uv 创建 Python 虚拟环境

在项目根目录执行：

``` cmd
uv venv
```

uv 会创建：

``` text
ai-engineering/
└── .venv/
```

`.venv` 是这个项目专属的 Python 虚拟环境。

### 为什么使用虚拟环境？

不同 Python 项目可能需要不同版本或不同依赖。

例如：

``` text
项目 A → requests 2.x
项目 B → requests 3.x
```

使用虚拟环境可以避免不同项目之间互相污染。

------------------------------------------------------------------------

## 8. 激活虚拟环境

Windows CMD：

``` cmd
.venv\Scripts\activate
```

成功后命令行前面出现：

``` text
(ai-engineering) C:\Users\29157\ai-engineering>
```

这表示当前已经进入项目虚拟环境。

------------------------------------------------------------------------

## 9. 检查虚拟环境中的 Python

``` cmd
python --version
```

结果：

``` text
Python 3.14.5
```

检查 Python 路径：

``` cmd
where python
```

第一条应该是：

``` text
C:\Users\29157\ai-engineering\.venv\Scripts\python.exe
```

这说明当前项目优先使用 `.venv` 中的 Python。

------------------------------------------------------------------------

## 10. 使用 VS Code 打开项目

在项目目录执行：

``` cmd
code .
```

VS Code 打开：

``` text
AI-ENGINEERING
```

### VS Code Python 解释器

按：

``` text
Ctrl + Shift + P
```

搜索：

``` text
Python: Select Interpreter
```

选择：

``` text
C:\Users\29157\ai-engineering\.venv\Scripts\python.exe
```

这样 VS Code 就会使用当前项目的 `.venv`。

------------------------------------------------------------------------

## 11. 安装 VS Code 扩展

推荐安装：

### Python

Microsoft 官方 Python 扩展。

### Pylance

用于 Python 类型检查、代码补全和智能提示。

### Ruff

用于 Python 代码检查和格式化。

### Error Lens

将代码错误和警告直接显示在代码行附近。

### GitLens

增强 VS Code 中的 Git 功能，例如查看：

-   Commit 历史
-   文件修改历史
-   某一行代码是谁修改的
-   分支信息

GitLens 登录并不是当前学习 Git 的必要条件，可以暂时跳过。

------------------------------------------------------------------------

## 12. 创建第一个 Python 程序

在项目根目录创建：

``` text
hello.py
```

代码：

``` python
print("Hello, AI Engineering!")
```

运行后：

``` text
Hello, AI Engineering!
```

这说明：

``` text
VS Code
   ↓
Python 解释器
   ↓
.venv
   ↓
hello.py
   ↓
成功运行
```

------------------------------------------------------------------------

## 13. 初始化 Git 仓库

在项目根目录：

``` cmd
git init
```

Git 会创建：

``` text
.git/
```

项目结构：

``` text
ai-engineering/
├── .git/
├── .venv/
└── hello.py
```

检查：

``` cmd
git status
```

------------------------------------------------------------------------

## 14. 配置 Git 用户信息

查看当前用户名：

``` cmd
git config --global user.name
```

查看邮箱：

``` cmd
git config --global user.email
```

最终设置为：

``` text
用户名：xu
邮箱：2915700929@qq.com
```

如果需要设置：

``` cmd
git config --global user.name "xu"
git config --global user.email "2915700929@qq.com"
```

### 注意

Git 用户名：

``` text
xu
```

和 GitHub 用户名：

``` text
xuxuxu121
```

不是同一个概念。

Git 用户名用于 Commit 作者信息；GitHub 用户名用于 GitHub
账户和仓库地址。

------------------------------------------------------------------------

## 15. 创建 `.gitignore`

项目根目录创建：

``` text
.gitignore
```

内容：

``` gitignore
.venv/
__pycache__/
*.pyc
```

作用：

-   `.venv/`：不提交 Python 虚拟环境
-   `__pycache__/`：不提交 Python 缓存
-   `*.pyc`：不提交 Python 编译缓存

检查：

``` cmd
git status
```

此时应该看到：

``` text
Untracked files:
    .gitignore
    hello.py
```

而不会看到 `.venv`。

------------------------------------------------------------------------

## 16. 第一次 Git Add

执行：

``` cmd
git add .
```

然后：

``` cmd
git status
```

应该看到：

``` text
Changes to be committed:

    new file:   .gitignore
    new file:   hello.py
```

这表示文件已经进入 Git 暂存区。

------------------------------------------------------------------------

## 17. 第一次 Git Commit

执行：

``` cmd
git commit -m "Initial commit"
```

成功结果类似：

``` text
[master (root-commit) 858143e] Initial commit
 2 files changed, 4 insertions(+)
 create mode 100644 .gitignore
 create mode 100644 hello.py
```

然后检查：

``` cmd
git status
```

成功结果：

``` text
On branch master
nothing to commit, working tree clean
```

------------------------------------------------------------------------

## 18. 将本地分支改为 main

执行：

``` cmd
git branch -M main
```

检查：

``` cmd
git branch
```

结果：

``` text
* main
```

------------------------------------------------------------------------

## 19. 创建 GitHub 仓库

GitHub 仓库：

``` text
ai-engineering
```

GitHub 用户名：

``` text
xuxuxu121
```

仓库地址：

``` text
https://github.com/xuxuxu121/ai-engineering.git
```

创建仓库时，因为本地已经有 Git 仓库和 Commit：

-   不需要创建 README
-   不需要添加 GitHub `.gitignore`
-   不需要添加 License

保持 GitHub 仓库为空，然后连接本地仓库。

------------------------------------------------------------------------

## 20. 添加 GitHub Remote

在本地项目目录：

``` cmd
git remote add origin https://github.com/xuxuxu121/ai-engineering.git
```

检查：

``` cmd
git remote -v
```

结果：

``` text
origin  https://github.com/xuxuxu121/ai-engineering.git (fetch)
origin  https://github.com/xuxuxu121/ai-engineering.git (push)
```

------------------------------------------------------------------------

## 21. 第一次 Push 到 GitHub

执行：

``` cmd
git push -u origin main
```

第一次 Push 可能要求：

``` text
please complete authentication in your browser...
```

按照浏览器中的 GitHub 登录/授权提示完成认证。

成功结果：

``` text
To https://github.com/xuxuxu121/ai-engineering.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.
```

这说明本地项目已经成功上传到 GitHub。

------------------------------------------------------------------------

## 22. 最终项目结构

本地：

``` text
ai-engineering/
│
├── .git/
│
├── .venv/
│   └── ...
│
├── .gitignore
│
└── hello.py
```

GitHub：

``` text
ai-engineering
├── .gitignore
└── hello.py
```

注意：

``` text
.venv/
```

不会上传到 GitHub，这是正确的。

------------------------------------------------------------------------

# 23. Git 基础工作流

以后开发 AI 项目，最常用的流程是：

``` text
修改代码
   ↓
git status
   ↓
git add .
   ↓
git commit -m "说明这次修改"
   ↓
git push
   ↓
GitHub
```

例如：

``` cmd
git status
git add .
git commit -m "Add new feature"
git push
```

------------------------------------------------------------------------

# 24. 常用 Git 命令

  命令                    作用
  ----------------------- --------------------------
  `git status`            查看当前状态
  `git init`              初始化 Git 仓库
  `git add .`             将修改加入暂存区
  `git commit -m "..."`   创建版本提交
  `git log`               查看 Commit 历史
  `git branch`            查看分支
  `git branch -M main`    将当前分支改为 main
  `git remote -v`         查看远程仓库
  `git push`              上传到 GitHub
  `git pull`              从远程仓库获取并合并更新
  `git clone`             克隆远程仓库
  `git diff`              查看代码修改
  `git restore`           恢复文件修改

------------------------------------------------------------------------

# 25. 本次学习成果

到目前为止，已经完成：

-   [x] 安装 Git
-   [x] 安装 Python
-   [x] 安装 VS Code
-   [x] 安装 uv
-   [x] 创建 `ai-engineering`
-   [x] 创建 `.venv`
-   [x] 激活虚拟环境
-   [x] 配置 VS Code Python 解释器
-   [x] 安装 Python / Pylance / Ruff / Error Lens / GitLens
-   [x] 创建第一个 Python 程序
-   [x] 初始化 Git
-   [x] 配置 Git 用户名和邮箱
-   [x] 创建 `.gitignore`
-   [x] 第一次 `git add`
-   [x] 第一次 `git commit`
-   [x] 修改分支为 `main`
-   [x] 创建 GitHub 仓库
-   [x] 配置 GitHub remote
-   [x] 第一次 `git push`
-   [x] 成功同步到 GitHub

------------------------------------------------------------------------

# 26. 下一阶段

接下来正式进入 AI Engineering 学习：

``` text
环境搭建
    ↓
Git / GitHub 基础
    ↓
Python 系统学习
    ↓
CS50P
    ↓
Python 项目
    ↓
API
    ↓
FastAPI
    ↓
LLM API
    ↓
RAG
    ↓
Agent
    ↓
AI 应用项目
    ↓
作品集 / GitHub
    ↓
求职
```

当前项目：

``` text
ai-engineering
```

将作为后续 AI 工程学习的基础仓库。
