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

    def history_zip(self) -> list:
        user_agent_messages = zip(self.history['user'], self.history['agent'])
        return user_agent_messages