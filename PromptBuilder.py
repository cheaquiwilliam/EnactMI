

def prompt_builder(
        prompt
        , read_first=True
        , role=''
        , expertise='20 years of experience'
        , learner=False
        , level='12 year old child'
        , step_by_step=False
        , explain_logic=False
        , explain_assumptions=False
        , code=False
        , program_language='Python==3.11'
        , step_by_step_code=False
        , include_function=False
        , docstring=False
        , comments=False
        , doctest=False
        , imports=False
        , elegant_code=False
        , snippet=False
        , snippet_content=''
        , just_code=False
        , exceptions=False
        , questions=False
):
    """
    Generates a response using the OpenAI ChatGPT model.

    Args:
        :param read_first: (bool) Tell LLM to read entire prompt before processing a response
        :param questions: (bool) Tell LLM to ask any question to help you accomplish the task
        :param exceptions: (bool) include try/except clauses where appropriate
        :param just_code: (bool) generate the program code
        :param elegant_code: (bool) evaluate code according to the 10 criteria
        :param imports: (bool) include any imported libraries used
        :param step_by_step_code: (bool) give step by step instructions (especially usefule for learning something new)
        :param snippet: (bool) can copy text to the prompt
        :param docstring: (bool) include a docstring with the code
        :param prompt: (str): The user's input prompt.
        :param role: (str): The role to act as. Defaults to an empty string.
        :param expertise: (str): The level of expertise to act as. Defaults to "20 years of experience".
        :param learner: (bool): Whether to explain the response as if to a learner. Defaults to False.
        :param level: (str): The level of the learner. Defaults to "12 year old child".
        :param step_by_step: (bool): Whether to provide step-by-step instructions. Defaults to False.
        :param explain_logic: (bool): Whether to explain the logic behind the response. Defaults to False.
        :param explain_assumptions: (bool): Whether to state and explain the assumptions made. Defaults to False.
        :param code: (bool): Whether to include code in the response. Defaults to False.
        :param doctest: (bool): include doctest with the code
        :param comments: (bool): include inline comments where appropriate
        :param include_function: (bool): tells Chatgpt to put the code inside of functions
        :param program_language: (str): The programming language to use in the code. Defaults to "Python==3.11".
        :param snippet.txt (bool): Whether to include a code snippet.txt in the response. Defaults to False.

    Returns:
        str: The generated response.

    """

    if role != '':
        prompt = f'Act like an {role} with {expertise}:\n' + prompt
    if read_first:
        prompt = """To optimize the performance and accuracy, please follow these instructions carefully:
1. Begin by reading the entire prompt comprehensively to gain a holistic understanding of the task at hand:
2. After reviewing the prompt in its entirety, execute prompts line by line, ensuring careful consideration and adherence to each instruction:
3. Pay close attention to detail and context throughout the execution process, maintaining a clear focus on the objectives and constraints outlined in the prompt:
""" + prompt
    if learner:
        prompt += f'\nExplain it as if to a {level}:'
    if step_by_step:
        prompt += '\nGive step by step instructions:'
    if explain_logic:
        prompt += '\nExplain your logic:'
    if explain_assumptions:
        prompt += '\nState and explain your assumptions:'
    if code:
        prompt += f'\nUse the {program_language} program language:'
    if step_by_step_code:
        prompt += '\nPerform the following steps:'
        prompt += '\n\tFirst, write the code:'
    if include_function:
        if step_by_step_code:
            prompt += '\n\tThen convert it to a function:'
        else:
            prompt += '\nthe output should be a function:'
    if docstring:
        if step_by_step_code:
            prompt += '\n\tThen add a docstring:'
        else:
            prompt += '\nEnsure to include a docstring:'
    if comments:
        if step_by_step_code:
            prompt += '\n\tThen add comments:'
        else:
            prompt += '\nEnsure to include comments:'
    if doctest:
        if step_by_step_code:
            prompt += '\n\tThen add doctest:'
        else:
            prompt += '\nEnsure to include doctest:'
    if imports:
        if step_by_step_code:
            prompt += '\n\tFinally add any imports used:'
        else:
            prompt += '\nEnsure to add any imports used'
    if exceptions:
        prompt += '\nBe sure to use try/except clauses appropriately'
    if elegant_code:
        prompt += """\nPerform each of the next 10 steps below in order, evaluating and reworking the code:
    1. Code Readability: Look for clear and well-structured code that is easy to understand. The code should be properly indented, have meaningful variable and function names, and follow a consistent coding style.
    2. Modular and Reusable Design: Check if the code follows the principles of modularity and reusability. Well-designed code should be divided into logical modules and functions that can be reused in different contexts without causing side effects.
    3. Performance and Efficiency: Assess if the code is optimized for performance and resource usage. Evaluate algorithms, loops, and data structures to ensure they are efficiently implemented. Avoid unnecessary computations and minimize memory consumption.
    4. Error Handling and Exception Handling: Check if the code handles errors and exceptions effectively. Look for proper error messages, logging of exceptions, and appropriate handling of edge cases to prevent unexpected crashes or incorrect behavior.
    5. Code Maintainability: Evaluate if the code is maintainable in the long term. Look for the presence of inline comments, useful documentation, and version control usage. Consider if the code can be easily updated, extended, or refactored without introducing bugs.
    6. Testability and Test Coverage: Assess if the code has unit tests and if the tests cover a significant portion of the codebase. Good code should have a comprehensive set of tests to ensure reliability and facilitate future modifications.
    7. Security Considerations: Check if the code follows secure coding practices. Look for proper input validation, protection against common vulnerabilities like SQL injection or cross-site scripting, and handling of sensitive data.
    8. Integration and Interoperability: Evaluate if the code interacts seamlessly with external systems or libraries. Check if it adheres to relevant standards, APIs, and protocols.
    9. Documentation: Assess if the code is well-documented, including inline comments, docstrings, and external documentation files. Good documentation helps other developers understand the code and accelerates onboarding.
    10. Code Consistency: Look for consistent coding patterns and adherence to design principles. Consistency in code style, naming conventions, and architectural choices is crucial for maintainability and collaboration.
"""

    if snippet:
        prompt += f'|||{snippet_content}|||'
    if include_function:
        prompt += '\nThe output should be a function:'
    if just_code:
        prompt += '\nGive the final output code:'
    if questions:
        prompt += '\nAsk any questions that will help you to accomplish this:'

    return prompt
