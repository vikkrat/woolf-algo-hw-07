from typing import List

class Comment:
    def __init__(self, text: str, author: str):
        self.text: str = text
        self.author: str = author
        self.replies: List[Comment] = []
        self.is_deleted: bool = False

    def add_reply(self, reply: 'Comment') -> None:
        self.replies.append(reply)

    def remove_reply(self) -> None:
        self.text = "Цей коментар було видалено."
        self.is_deleted = True

    def display(self, indent: str = '') -> None:
        print(f"{indent}{self.author}: {self.text}")
        for reply in self.replies:
            reply.display(indent + '    ')

# Приклад використання:
root_comment = Comment("Яка чудова книга!", "Бодя")
reply1 = Comment("Книга повне розчарування :(", "Андрій")
reply2 = Comment("Що в ній чудового?", "Марина")

root_comment.add_reply(reply1)
root_comment.add_reply(reply2)

reply1_1 = Comment("Не книжка, а перевели купу паперу ні на що...", "Сергій")
reply1.add_reply(reply1_1)

reply1.remove_reply()

root_comment.display()
