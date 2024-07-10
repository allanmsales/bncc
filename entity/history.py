class History:
    """Class to store the chat history"""
    def __init__(self):
        self.history = {
            'user': [],
            'agent': []
            }

    def add_to_history_agent(self, answer) -> None:
        """Add an agent's answer to chat history"""
        self.history['agent'].append(answer)

    def add_to_history_user(self, question) -> None:
        """Add an user's answer to chat history"""
        self.history['user'].append(question)
