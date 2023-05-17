class PromptBuilder:

    def __init__(self) -> None:
        pass


    def load_profile(self, prompt_profile:str = '') -> dict:
        """Loads the prompt profile from the specified file.

        Args:
            prompt_profile (str, optional): The path to the prompt profile file. Defaults to ''.

        Returns:
            dict: The loaded prompt profile.
        """
        
        # Load the prompt profile and use defaults if that fails.
        try:
            with open(prompt_profile, 'r') as f:
                prompt_profile = json.load(f)
        except:
            prompt_profile = self.DEFAULT_PROMPT

        return prompt_profile
    

    def remove_whitespace(self, text:str) -> str:
        """
        Flatten multiple whitespace characters into a single space.

        Args:
            text (str): The text to remove whitespace from.

        Returns:
            str: The text with extra whitespace removed.
        """

        return " ".join(text.split())