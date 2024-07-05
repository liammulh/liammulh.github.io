# {{ cv.basic_info.name }}

{{ cv.basic_info.phone }} | {{ cv.basic_info.email }} | {{ cv.basic_info.location }}

## Experience
{% for exp in cv.experience %}
### {{ exp.title }} - {{ exp.employer }}

{{ exp.start }} - {{ exp.end }} | {{ exp.location }}

{% for resp in exp.responsibilities -%}
- {{ resp }}
{% endfor %} {# End responsibilities loop. #}
{%- endfor %} {# End experience loop. #}
## Education
{% for edu in cv.education %}
### {{ edu.degree }} - {{ edu.institution }}

{{ edu.start }} - {{ edu.end }}

{% for note in edu.notes -%}
- {{ note }}
{% endfor %} {# End notes loop. #}
{%- endfor %} {# End experience loop. #}
