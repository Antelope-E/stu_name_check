# 学生实验报告提交检查工具

学生实验报告提交检查工具是一个Python脚本，用于自动检测学生是否按照规定格式提交了文件，并将这些文件按学生姓名分类到不同的文件夹中。此外，该工具还能生成一个txt报告文档，列出未按格式要求提交实验报告或未提交实验报告的学生名单。

## 环境要求

- Python 3.7 或更高版本
- pandas
- fsspec
- openpyxl

## 安装Python

1. **下载Python**：访问[Python官网](https://www.python.org/downloads/)下载Python安装程序。选择与您操作系统相匹配的版本进行下载。

2. **安装Python**：运行下载的安装程序。在安装过程中，请确保勾选“Add Python to PATH”的选项，以便于在命令行中直接运行Python。

## 安装PyCharm

PyCharm是一个功能强大的Python IDE，对于Python项目的开发非常有帮助。

1. **下载PyCharm**：访问[JetBrains官网](https://www.jetbrains.com/pycharm/download/)下载PyCharm安装程序。您可以选择免费的Community版本或者专业的Pro版本。

2. **安装PyCharm**：运行下载的安装程序并按照指示完成安装。

## 下载源代码

1. **克隆或下载代码**：访问项目的GitHub页面，使用`git clone`命令或直接下载源代码压缩包。

2. **打开项目**：启动PyCharm，选择"Open"，然后导航到您刚刚克隆或解压的项目目录，打开项目。

## 安装项目依赖

1. **打开终端**：在PyCharm中，通常可以在底部找到"Terminal"标签页，点击打开项目的终端。

2. **安装依赖**：在终端中执行以下命令，安装项目所需的依赖：

    ```bash
    pip install -r requirements.txt
    ```

## 修改和运行脚本

1. **查看代码注解**：打开`stu_name_check.py`，阅读代码中的注解，修改为自己的路径。

2. **运行脚本**：在PyCharm中，右键点击`stu_name_check.py`文件并选择"Run"来执行脚本。也可以在终端中使用以下命令运行：

    ```bash
    python stu_name_check.py
    ```

3. **查看结果**：根据脚本输出的指示，查看生成的"未提交.txt"文件以及分类后的学生文件夹。

## 关键变量说明

**roster_path：** Excel花名册路径（包含学号和姓名列）

**folder_path：** 学生提交的所有实验报告汇总文件夹的路径，文件夹内为分散文件，不内嵌额外文件夹

**N：** 老师要求提交的实验报告数量，如到了期末一共有五个实验报告，则N=5

## 注意事项

- 在运行脚本前，请确保已正确设置Python环境并安装了所有依赖。
- 根据脚本中的注释调整路径和其他配置项以匹配您的项目结构和需求。