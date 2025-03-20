from rich import print
from rich.tree import Tree
from pathlib import Path

def build_tree(root_path: Path, tree: Tree) -> None:
    try:
        for entry in root_path.iterdir():
            if entry.is_dir():
                branch = tree.add(f"[bold blue]{entry.name}[/]")
                build_tree(entry, branch)
            else:
                tree.add(entry.name)
    except PermissionError:
        tree.add("[red]Permission Denied[/red]")

if __name__ == "__main__":
    user_input = input("Enter the path to visualize: ")
    try:
        if user_input == "":
            user_input = "/mnt/c/Users/MuhammadSaqib/Documents/DataPipelineV2_spring_server"
        # Create a Path object from the user input. expanduser and resolve
        # help normalize the path (e.g. handling ~ and relative paths)
        path = Path(user_input).expanduser().resolve()
        tree = Tree(f"[green]{str(path)}[/green]")
        build_tree(path, tree)
        print(tree)
    except:
        print("[red]Invalid Path![/red]")
