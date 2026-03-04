import pathlib
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

def convert_images():
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True)

    input_dir_path = filedialog.askdirectory(title="【元データ】フォルダを選択")
    if not input_dir_path: return

    output_dir_path = filedialog.askdirectory(title="【保存先】フォルダを選択")
    if not output_dir_path: return

    input_dir = pathlib.Path(input_dir_path)
    output_dir = pathlib.Path(output_dir_path)
    
    count = 0
    # フォルダ内の全ファイルをチェック
    for file in input_dir.iterdir():
        if file.is_file():
            try:
                # 拡張子で判断せず、とりあえず開いてみる
                with Image.open(file) as img:
                    count += 1
                    
                    # JPG変換用にRGBモードへ（透過対策）
                    rgb_img = img.convert("RGB")
                    
                    # 保存（連番リネーム）
                    new_filename = f"image_{count}.jpg"
                    save_path = output_dir / new_filename
                    
                    rgb_img.save(save_path, "JPEG", quality=90)
                    print(f"成功: {file.name} -> {new_filename}")
            except (IOError, SyntaxError):
                # 画像として開けないファイル（テキスト等）は無視する
                print(f"スキップ（非画像）: {file.name}")
            except Exception as e:
                print(f"エラー（{file.name}）: {e}")

    messagebox.showinfo("完了", f"{count}枚の画像を変換しました。")

if __name__ == "__main__":
    convert_images()