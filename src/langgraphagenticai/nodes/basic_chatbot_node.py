from src.langgraphagenticai.state.state import State


class BasicChatbotNode:
    """
    Basic chatbot login implementation
    """
    def __init__(self,model):
        self.llm=model

    def process(self, state:State)->dict:
        """
        Processes the input state nd generates a chatbot response
        """
        return {"messages":self.llm.invoke(state['messages'])}
    
        
