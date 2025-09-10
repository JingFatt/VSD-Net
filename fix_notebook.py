import nbformat

notebook_path = "UIEB_Code.ipynb"  # 改成你的 notebook 文件名
fixed_path = "VSD-Net.ipynb"

with open(notebook_path, "r", encoding="utf-8") as f:
    nb = nbformat.read(f, as_version=nbformat.NO_CONVERT)

for cell in nb.cells:
    metadata = cell.get("metadata", {})
    if "widgets" in metadata:
        metadata["widgets"]["state"] = {}

with open(fixed_path, "w", encoding="utf-8") as f:
    nbformat.write(nb, f)

print(f"修复完成，生成文件: {fixed_path}")
