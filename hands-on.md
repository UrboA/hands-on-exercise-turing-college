# Part 4: Hands-on - Repository Refactoring

![](https://imgur.com/rjZavyI.jpg)

Have you ever wondered how developers join existing projects and start contributing meaningful code quickly? Or how teams manage to work on the same codebase without stepping on each other's toes? In this hands-on exercise, you'll step into the shoes of a developer who just joined a project and needs to make significant improvements to an existing codebase.

You'll be working with a simple [Dungeons & Dragons (D&D)](https://en.wikipedia.org/wiki/Dungeons_%26_Dragons#Play_overview) combat game that, while functional, needs quite a bit of love. The code works, but it's not using any of the professional practices we've learned about - no type hints, minimal documentation, and a structure that makes adding new features difficult. Your task will be to transform this code into something that would make any senior developer proud!

What makes this exercise particularly exciting is that you'll be using the same tools and workflows that professional developers use every day. You'll create feature branches, write meaningful commit messages, and use AI coding assistants to help you understand and improve the code faster. This is exactly how modern development teams work!

The goal isn't just to make the code better - it's to practice the real-world workflows that will make you a valuable team member in any development project. By the end of this exercise, you'll have hands-on experience with:
- Working with an existing codebase
- Using Git for version control in a professional way
- Leveraging AI tools to accelerate your development
- Applying everything you've learned about clean code and testing

Ready to turn some rough code into a polished gem? Let's dive in!

## Task Description

You've inherited a simple text-based Dungeons & Dragons combat game that needs modernizing. While the game works, it's missing many professional development practices we've learned about. Your mission is to refactor and improve this codebase using proper version control, type hints, testing, and object-oriented design.

> **Note about D&D**: Dungeons & Dragons (D&D) is a fantasy role-playing game where players create characters with different abilities (like strength and dexterity) and engage in combat using dice rolls to determine outcomes. Don't worry if you're not familiar with D&D - this project uses a very simplified version of its mechanics, and all the game rules you need to know are implemented in the code!
> 
> This is actually a great simulation of real-world development, where you often need to work on projects in industries or domains you're not familiar with. Just as you can improve this codebase without being a D&D expert, developers regularly enhance financial, medical, or e-commerce systems without deep domain expertise. The key is understanding the code itself and gradually learning the domain concepts as needed.

Your task is to donwload the repository and fulfill the requirements listed in the TODO.txt file. The goal is to practice real-world development workflows while improving code quality and adding features.

### Getting Started
1. Download the repository contents from [here]()
2. Copy the contents into a new directory and initialize a Git repository
3. Read the README.md file to understand the project and the requirements

### Required Improvements

The improvements needed are listed in a TODO.txt file in the repository.

### Git Workflow Requirements

1. Initialize a Git repository
2. For each feature/fix:
   - Create a new branch from the main branch
   - Implement the change
   - Write appropriate commit messages
   - (Optional) Create a pull request to merge into main
   - Merge the branch into main after reviewing it

### AI Coding Assistants

For this exercise, you are required to use at least one AI coding assistant to help you understand and improve the codebase. These tools will significantly accelerate your development process and help you learn professional coding practices. Here are the recommended tools:

#### AI-Enhanced IDEs:
- **[Cursor](https://www.cursor.com)**: A powerful AI-powered IDE that helps with code understanding, refactoring, and documentation
- **[GitHub Copilot](https://github.com/features/copilot)**: Directly integrates into VS Code, providing real-time code completion and suggestions

#### Online Chat Assistants:
- **[Claude](https://claude.ai) and [ChatGPT](https://chat.openai.com)**: Powerful chat-based AI assistants that excel at explaining code, generating documentation, and providing detailed code explanations


Remember that these tools are assistants, not replacements for your own understanding. You should:
- Review and understand all suggested code
- Modify suggestions to match your needs
- Use AI to learn about Python features you're not familiar with

#### Example: Using Cursor for Type Hints and Docstrings

Here's an example of how can you use the AI-enhanced IDE [Cursor](https://www.cursor.com) to help you add type hints and docstrings to existing code. We'll use the Character class as an example.

##### 1. Understanding the Code

First, before asking Cursor to help you or make edits, it's best to understand the code you're working with. Open the `character.py` file, make sure that it's present in the Cursor context. Then, ask Cursor to explain what it does.

![Asking Cursor to explain code](https://i.imgur.com/CgTOAcg.gif)

##### 2. Adding Type Hints
Prompt Cursor to add type hints to the code. Go through the suggestions, which you can accept or reject, or if the whole file looks good, you can just press 'Accept File' to add all the changes at once.

![Adding type hints with Cursor](https://i.imgur.com/SRy62Bn.gif)

##### 3. Adding Docstrings
Next, we can ask Cursor to generate comprehensive docstrings in the style we want (for example, Google style format):

![Adding docstrings with Cursor](https://i.imgur.com/KtaTQ97.gif)

#### Tips for Working with AI Tools
- Be specific in your prompts
- Always review and understand the suggested code
- Iterate and clarify the suggestions if the first suggestion isn't perfect

## Tips for Success in this Hands-on Exercise

1. **Start Small**: Begin with type hints and docstrings - these changes are relatively isolated and good practice for Git workflows
2. **Use AI Wisely**: Ask AI tools to explain code sections you don't understand, but write the bigger implementations yourself
3. **Test Early**: Write tests before making major changes to ensure you don't break existing functionality
4. **Commit Often**: Make small, focused commits with clear messages
5. **Ask for Help**: Use peer programming sessions to learn from others' approaches

Remember: The goal isn't just to complete the tasks, but to practice professional development workflows and tools you'll use in real projects.

## Approach to Solving the Task

Take a similar approach as in previous hands-on exercises:
1. Spend 3-4 hours attempting the task independently
2. If stuck, spend up to 10 hours working with peers and JTLs
3. If still stuck, review the suggested solution and ensure you understand it fully

---

[SOLUTION](link_to_solution)