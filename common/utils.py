from pathlib import Path


def get_home_path():
    home_path = Path(__file__).parent.parent
    attachment_path = home_path.joinpath("attachments")

    if attachment_path.exists():
        attachment_path.mkdir(parents=True)

    return attachment_path