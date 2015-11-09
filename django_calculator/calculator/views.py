from django.shortcuts import render_to_response

__author__ = 'MatthewBarnette'

def math(request):
    first = request.GET.get('first_number')
    second = request.GET.get('second_number')
    operator = request.GET.get('operator')
    op_dict = {'plus': "+", 'minus': "-", 'multiply': "*", 'divided': '/'}
    if operator is None:
        context = {'answer': ''}
        return render_to_response(template_name='calculator.html', context=context)
    else:
        equation = first + op_dict[operator] + second
        try:
            answer = float(eval(equation))
        except:
            context = {'answer': 'Cannot be calculated!!'}
            return render_to_response(template_name='calculator.html', context=context)
    context = {'answer': answer}
    return render_to_response(template_name='calculator.html', context=context)

def test(request):
    return render_to_response(template_name='test.html')