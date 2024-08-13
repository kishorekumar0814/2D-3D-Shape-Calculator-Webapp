from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/shapes/<shape_type>')
def shapes(shape_type):
    shapes_dict = {
        '2d': ['square', 'circle', 'rectangle', 'triangle', 'ellipse'],
        '3d': ['cube', 'sphere', 'cylinder', 'cone', 'pyramid']
    }
    shapes_list = shapes_dict.get(shape_type, [])
    return render_template('shapes.html', shape_type=shape_type, shapes_list=shapes_list)

@app.route('/shapes/<shape_type>/<shape_name>', methods=['GET', 'POST'])
def shape_details(shape_type, shape_name):
    result = {}
    if request.method == 'POST':
        if shape_name == 'square':
            side = float(request.form.get('side'))
            result['area'] = side ** 2
        elif shape_name == 'circle':
            radius = float(request.form.get('radius'))
            result['area'] = 3.14159 * (radius ** 2)
        elif shape_name == 'rectangle':
            length = float(request.form.get('length'))
            width = float(request.form.get('width'))
            result['area'] = length * width
        elif shape_name == 'triangle':
            base = float(request.form.get('base'))
            height = float(request.form.get('height'))
            result['area'] = 0.5 * base * height
        elif shape_name == 'ellipse':
            semi_major_axis = float(request.form.get('semi_major_axis'))
            semi_minor_axis = float(request.form.get('semi_minor_axis'))
            result['area'] = 3.14159 * semi_major_axis * semi_minor_axis
        elif shape_name == 'cube':
            side = float(request.form.get('side'))
            result['area'] = 6 * (side ** 2)
            result['volume'] = side ** 3
        elif shape_name == 'sphere':
            radius = float(request.form.get('radius'))
            result['area'] = 4 * 3.14159 * (radius ** 2)
            result['volume'] = (4 / 3) * 3.14159 * (radius ** 3)
        elif shape_name == 'cylinder':
            radius = float(request.form.get('radius'))
            height = float(request.form.get('height'))
            result['area'] = 2 * 3.14159 * radius * (radius + height)
            result['volume'] = 3.14159 * (radius ** 2) * height
        elif shape_name == 'cone':
            radius = float(request.form.get('radius'))
            height = float(request.form.get('height'))
            slant_height = (radius ** 2 + height ** 2) ** 0.5
            result['area'] = 3.14159 * radius * (radius + slant_height)
            result['volume'] = (1 / 3) * 3.14159 * (radius ** 2) * height
        elif shape_name == 'pyramid':
            base_length = float(request.form.get('base_length'))
            base_width = float(request.form.get('base_width'))
            height = float(request.form.get('height'))
            slant_height = ((base_length / 2) ** 2 + height ** 2) ** 0.5
            result['area'] = base_length * base_width + 2 * base_length * slant_height
            result['volume'] = (1 / 3) * base_length * base_width * height
        
        if request.form.get('calculate_volume') == 'on':
            return render_template('result.html', shape_name=shape_name, result=result)
        else:
            result.pop('volume', None)  # Remove volume if not needed
            return render_template('result.html', shape_name=shape_name, result=result)

    return render_template('shape_details.html', shape_type=shape_type, shape_name=shape_name)

if __name__ == '__main__':
    app.run(debug=True)
