```markdown
# LUMA-LAMMA Development Patterns

> Auto-generated skill from repository analysis

## Overview
This skill teaches you the core development patterns and conventions used in the LUMA-LAMMA Python codebase. You'll learn how to structure files, write imports and exports, follow commit message conventions, and organize tests. This guide will help you contribute code that is consistent with the project's established practices.

## Coding Conventions

### File Naming
- Use **camelCase** for file names.
  - **Example:** `dataLoader.py`, `modelTrainer.py`

### Import Style
- Use **relative imports** within the package.
  - **Example:**
    ```python
    from .utils import calculateScore
    from .dataLoader import loadData
    ```

### Export Style
- Use **named exports** by specifying `__all__` in modules.
  - **Example:**
    ```python
    __all__ = ['trainModel', 'evaluateModel']
    ```

### Commit Messages
- Follow the **conventional commits** pattern.
- Use the `feat` prefix for new features.
- Keep commit messages concise (average ~38 characters).
  - **Example:**  
    ```
    feat: add support for batch processing
    ```

## Workflows

### Adding a New Feature
**Trigger:** When implementing a new functionality  
**Command:** `/add-feature`

1. Create a new Python file using camelCase naming.
2. Implement your feature using relative imports as needed.
3. Export your main functions/classes using `__all__`.
4. Write corresponding tests in a `*.test.*` file.
5. Commit your changes with a message starting with `feat:`.

### Writing Tests
**Trigger:** When testing new or existing code  
**Command:** `/write-test`

1. Create a test file matching the pattern `*.test.*` (e.g., `dataLoader.test.py`).
2. Write test functions for your code.
3. Use the project's preferred (unknown) testing framework or standard Python assertions.
4. Run your tests to ensure correctness.

### Refactoring Code
**Trigger:** When improving or restructuring existing code  
**Command:** `/refactor`

1. Update file and function names to use camelCase if needed.
2. Adjust imports to use relative paths.
3. Ensure all exports are named via `__all__`.
4. Update or add tests as necessary.
5. Commit with an appropriate message (e.g., `feat: refactor data loader logic`).

## Testing Patterns

- Test files follow the `*.test.*` naming convention.
  - **Example:** `modelTrainer.test.py`
- The specific testing framework is not detected; use standard Python testing practices.
- Place tests alongside or near the code they validate.

**Example Test:**
```python
def test_trainModel():
    result = trainModel(data)
    assert result is not None
```

## Commands
| Command        | Purpose                                     |
|----------------|---------------------------------------------|
| /add-feature   | Scaffold and document a new feature         |
| /write-test    | Create and run tests for your code          |
| /refactor      | Refactor code to match project conventions  |
```
