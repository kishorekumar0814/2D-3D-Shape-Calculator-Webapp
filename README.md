# 2D-3D-Shape-Calculator-Webapp

## Overview

This project is a web application built with Python Flask, HTML, and CSS that calculates the area and/or volume of 2D and 3D shapes. Users can select from a list of shapes, input dimensions, and get results for area and volume (for 3D shapes). The app provides an interactive user interface with a clean and modern design.

## Features

- **2D Shapes**: Square, Circle, Rectangle, Triangle, Ellipse
- **3D Shapes**: Cube, Sphere, Cylinder, Cone, Pyramid
- Calculate Area for 2D shapes
- Calculate Area and Volume for 3D shapes
- User-friendly interface with navigation and form validation

## Project Structure

    /your_project
      /static
        styles.css # CSS styles for the application
      /templates
        home.html # Homepage with options to select 2D or 3D shapes
        shapes.html # Page listing shapes based on type (2D or 3D)
        shape_details.html # Page with form to input dimensions for selected shape
        result.html # Page displaying the calculation results
        app.py # Flask application script
        requirements.txt # List of project dependencies
        README.md # Project documentation


## Setup

### Prerequisites

Ensure you have Python 3.6 or later installed on your system.

### Creating a Virtual Environment

1. **Create a virtual environment:**

    ```bash
    python3 -m venv venv
    ```

2. **Activate the virtual environment:**

    - **On Windows:**

      ```bash
      venv\Scripts\activate
      ```

    - **On macOS/Linux:**

      ```bash
      source venv/bin/activate
      ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

1. **Start the Flask development server:**

    ```bash
    python app.py
    ```

2. **Open your web browser and navigate to:**

    ```
    http://127.0.0.1:5000/
    ```

## Usage

1. **Homepage**: Choose between 2D Shapes or 3D Shapes.
2. **Shapes Page**: Select a specific shape to calculate.
3. **Shape Details Page**: Enter dimensions and select if you want to calculate volume (for 3D shapes).
4. **Results Page**: View the calculated area and/or volume.

## Development

- **Modify HTML/CSS**: Update the `templates` and `static/styles.css` files for changes in UI and styling.
- **Update Flask Routes**: Modify `app.py` to add or change routes and functionality.

## Contributing

Feel free to submit issues or pull requests if you would like to contribute to this project. Please ensure that your contributions adhere to the project's coding style and include appropriate tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please contact [Mail Me](mailto:kishorekumar1409@gmail.com).

## Note
This project still in development - If you find any issue raise me out and to complete it. Thank You! :-)
