## Contribution Process

### Step 1: Open an Issue

- Before contributing, search the project's issue tracker to ensure the problem you're encountering or the enhancement you're suggesting isn't already listed.
- If it's something new, submit an issue describing the bug fix or enhancement you propose. Be as detailed as possible to assist others in understanding your intentions and the scope of the issue.

### Step 2: Fork and Create a Branch

- Clone your the repository to your local machine:
  
  ```sh
  git clone https://git.tonic-ai.com/positonic/EasyRealEstate/EasyRealEstate.git
  cd EasyRealEstate
  ```

- Create a new branch for your fix or feature. Naming your branch as `feature/<feature-name>` or `bugfix/<bug-name>` helps in identifying the purpose of your branch:

  ```sh
  git checkout -b feature/add-new-analysis
  ```

### Step 3: Make Changes

- Implement your bug fix or feature following the coding guidelines provided in the repository.
- Ensure that your code adheres to the existing style to keep the project consistent and maintainable.

### Step 4: Test Your Changes

- Add tests for your changes to ensure that your code works as intended and to prevent future regressions.
- Run all the existing tests to make sure previous functionality isn’t broken:

  ```bash
  python -m unittest discover -s tests
  ```

### Step 5: Add Example Usage

- Enhance the documentation or examples folder with example usage of new features or demonstrating how the bug has been fixed, allowing other users to understand and effectively use the changes.

### Step 6: Submit a Pull Request

- Commit your changes with a meaningful commit message. This helps others to understand the purpose of the changes quickly:

  ```sh
  git commit -am "Add new financial analysis feature"
  ```

- Push your branch to your forked repository:

  ```sh
  git push origin feature/add-new-analysis
  ```

- Go to your forked repository on GitLab and click `Create merge request`. Target the main branch of the original repository when you make the pull request.
- Provide a clear and detailed description of the pull request, linking back to any related issues.

## Join Team Tonic

Team Tonic and Tonic-AI are dedicated to building and enhancing technologies. By contributing to `EasyRealEstate`, you become a part of an innovative community that values collaboration and creativity. We appreciate your contributions and look forward to growing together!

Join us and contribute to making `EasyRealEstate` the best tool for real estate investment analysis on the market!