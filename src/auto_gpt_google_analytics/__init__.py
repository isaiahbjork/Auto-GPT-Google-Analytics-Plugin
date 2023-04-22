"""This is a plugin to use Auto-GPT with MetaTrader."""
from typing import Any, Dict, List, Optional, Tuple, TypeVar, TypedDict, Union
from auto_gpt_plugin_template import AutoGPTPluginTemplate

# Google Analytics
import os
from gaapi4py import GAClient

c = GAClient()

PromptGenerator = TypeVar("PromptGenerator")

os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
view_id = os.environ('GOOGLE_ANALYTICS_VIEW_ID')


class Message(TypedDict):
    role: str
    content: str


class AutoGPTGoogleAnalyticsPlugin(AutoGPTPluginTemplate):
    """
    This is a plugin to use Auto-GPT with Google Analytics.
    """

    def __init__(self):
        super().__init__()
        self._name = "Auto-GPT-Google-Analytics"
        self._version = "0.1.0"
        self._description = "This is a plugin for Auto-GPT-Google-Analytics."

    def post_prompt(self, prompt: PromptGenerator) -> PromptGenerator:
        prompt.add_command(
            "Get Website Analytics",
            "google_analytics",
            {
                "metric": "<metric>",
                "start_date": "<start_date>",
                "end_date": "<end_date>"
            },
            self.google_analytics
        ),
        return prompt

    def can_handle_post_prompt(self) -> bool:
        """This method is called to check that the plugin can
        handle the post_prompt method.
        Returns:
            bool: True if the plugin can handle the post_prompt method."""
        return True

    def can_handle_on_response(self) -> bool:
        """This method is called to check that the plugin can
        handle the on_response method.
        Returns:
            bool: True if the plugin can handle the on_response method."""
        return False

    def on_response(self, response: str, *args, **kwargs) -> str:
        """This method is called when a response is received from the model."""
        pass

    def can_handle_on_planning(self) -> bool:
        """This method is called to check that the plugin can
        handle the on_planning method.
        Returns:
            bool: True if the plugin can handle the on_planning method."""
        return False

    def on_planning(
        self, prompt: PromptGenerator, messages: List[Message]
    ) -> Optional[str]:
        """This method is called before the planning chat completion is done.
        Args:
            prompt (PromptGenerator): The prompt generator.
            messages (List[str]): The list of messages.
        """
        pass

    def can_handle_post_planning(self) -> bool:
        """This method is called to check that the plugin can
        handle the post_planning method.
        Returns:
            bool: True if the plugin can handle the post_planning method."""
        return False

    def post_planning(self, response: str) -> str:
        """This method is called after the planning chat completion is done.
        Args:
            response (str): The response.
        Returns:
            str: The resulting response.
        """
        pass

    def can_handle_pre_instruction(self) -> bool:
        """This method is called to check that the plugin can
        handle the pre_instruction method.
        Returns:
            bool: True if the plugin can handle the pre_instruction method."""
        return False

    def pre_instruction(self, messages: List[Message]) -> List[Message]:
        """This method is called before the instruction chat is done.
        Args:
            messages (List[Message]): The list of context messages.
        Returns:
            List[Message]: The resulting list of messages.
        """
        pass

    def can_handle_on_instruction(self) -> bool:
        """This method is called to check that the plugin can
        handle the on_instruction method.
        Returns:
            bool: True if the plugin can handle the on_instruction method."""
        return False

    def on_instruction(self, messages: List[Message]) -> Optional[str]:
        """This method is called when the instruction chat is done.
        Args:
            messages (List[Message]): The list of context messages.
        Returns:
            Optional[str]: The resulting message.
        """
        pass

    def can_handle_post_instruction(self) -> bool:
        """This method is called to check that the plugin can
        handle the post_instruction method.
        Returns:
            bool: True if the plugin can handle the post_instruction method."""
        return False

    def post_instruction(self, response: str) -> str:
        """This method is called after the instruction chat is done.
        Args:
            response (str): The response.
        Returns:
            str: The resulting response.
        """
        pass

    def can_handle_pre_command(self) -> bool:
        """This method is called to check that the plugin can
        handle the pre_command method.
        Returns:
            bool: True if the plugin can handle the pre_command method."""
        return False

    def pre_command(
        self, command_name: str, arguments: Dict[str, Any]
    ) -> Tuple[str, Dict[str, Any]]:
        """This method is called before the command is executed.
        Args:
            command_name (str): The command name.
            arguments (Dict[str, Any]): The arguments.
        Returns:
            Tuple[str, Dict[str, Any]]: The command name and the arguments.
        """
        pass

    def can_handle_post_command(self) -> bool:
        """This method is called to check that the plugin can
        handle the post_command method.
        Returns:
            bool: True if the plugin can handle the post_command method."""
        return False

    def post_command(self, command_name: str, response: str) -> str:
        """This method is called after the command is executed.
        Args:
            command_name (str): The command name.
            response (str): The response.
        Returns:
            str: The resulting response.
        """
        pass

    def can_handle_chat_completion(
        self, messages: Dict[Any, Any], model: str, temperature: float, max_tokens: int
    ) -> bool:
        """This method is called to check that the plugin can
          handle the chat_completion method.
        Args:
            messages (List[Message]): The messages.
            model (str): The model name.
            temperature (float): The temperature.
            max_tokens (int): The max tokens.
          Returns:
              bool: True if the plugin can handle the chat_completion method."""
        return False

    def handle_chat_completion(
        self, messages: List[Message], model: str, temperature: float, max_tokens: int
    ) -> str:
        """This method is called when the chat completion is done.
        Args:
            messages (List[Message]): The messages.
            model (str): The model name.
            temperature (float): The temperature.
            max_tokens (int): The max tokens.
        Returns:
            str: The resulting response.
        """
        pass

    def google_analytics(self, metric: str, start_date: str, end_date: str) -> Union[int, str]:
        metric = f'ga:{metric}'
        # Build the request body
        request_body = {
            'view_id': view_id,  # Replace with your Google Analytics view ID
            'start_date': start_date,
            'end_date': end_date,
            'dimensions': {
                'ga:sourceMedium',
                'ga:date'
            },
            'metrics': {
                metric
            }
        }

        try:
            # Get the GA data
            response = c.get_all_data(request_body)
            data = response['data']

            # Aggregate the metric values
            total = data['data'][metric].astype(int).sum()
            return total
        except KeyError:
            return f'{metric} is not a valid metric.'
        except Exception as e:
            return f'An error occurred: {str(e)}'

    def get_metrics_from_file(self):
        try:
            with open("metrics.txt", 'r') as file:
                metrics = file.readlines()
            return [metric.strip() for metric in metrics]
        except FileNotFoundError:
            print("Metrics file not found.")
            return []

    def metric_exists(self, metric: str) -> bool:
        try:
            metrics = self.get_metrics_from_file()
            if metric in metrics:
                return f"{metric} exists."
            else:
                return f"{metric} does not exist."
        except Exception as e:
            print(f"Error checking metric: {str(e)}")
            return f"Error checking metric: {str(e)}"
