from telethon.sync import TelegramClient, events
from tqdm import tqdm
import os
from telethon.tl.types import (
    MessageMediaPhoto,
    MessageMediaDocument,
    DocumentAttributeFilename,
    DocumentAttributeVideo,
)


def gen_file_name(msg):
    if type(msg.media) == MessageMediaDocument:
        attributes = msg.media.document.attributes
        atts = [a for a in attributes if type(a) == DocumentAttributeFilename]
        if atts:
            return atts[0].file_name
    return msg.date.strftime("%Y%m%d_%H:%M:%S")


def should_download(media):
    if type(media) == MessageMediaPhoto:
        return True
    elif type(media) == MessageMediaDocument:
        attributes = media.document.attributes
        if media.document.mime_type != "application/x-tgsticker":
            if [
                a
                for a in attributes
                if type(a) == DocumentAttributeFilename and "gif" not in a.file_name
            ]:
                return True
    return False


def main():
    api_id = 
    api_hash = ""

    with TelegramClient("asd", api_id, api_hash) as client:
        messages = client.get_messages(
            "GROUP_NAME", limit=33300
        )  # limit defaults to 1
        # messages = client.get_messages("Stefan Ionut Ilie")  # limit defaults to 1
        for msg in tqdm(messages):
            if (
                type(msg.media) == MessageMediaPhoto
                or type(msg.media) == MessageMediaDocument
            ):
                file_name = gen_file_name(msg)
                if should_download(msg.media):
                    msg.download_media(file=os.path.join("media", file_name))


if __name__ == "__main__":
    main()
