/**
 * Generated {{ resource.title }}.js code. Edit at own risk.
 * When regenerated the changes will be lost.
**/
import React from 'react';
import {
    List,
    Show,
    Edit,
    Create,
    Datagrid,
    SimpleShowLayout,
    SimpleForm,
    {% for import in resource.imports %}
    {{ import }},
    {% endfor %}
    DisabledInput,
    DeleteButton,
    EditButton,
    ShowButton
} from 'admin-on-rest';
{% if resource.filters %}
import {
    {{ resource.title }}Filter
} from './Filters';
{% endif %}

{% if resource.create %}
const validationCreate{{ name }} = values => {
    const errors = {};
    {% for attribute in resource.create %}
    {% if attribute.required %}
    if (!values.{{ attribute.source }}) {
        errors.{{ attribute.source }} = ["{{ attribute.source }} is required"];
    }
    {% endif %}
    {% endfor %}
    return errors;
}

{% endif %}
{% if resource.edit %}
const validationEdit{{ name }} = values => {
    const errors = {};
    {% for attribute in resource.edit %}
    {% if attribute.required %}
    if (!values.{{ attribute.source }}) {
        errors.{{ attribute.source }} = ["{{ attribute.source }} is required"];
    }
    {% endif %}
    {% endfor %}
    return errors;
}

{% endif %}
{% if resource.create %}
{% for attribute in resource.create %}
{% if attribute.choices %}
const createchoice{{ attribute.source }} = [
    {% if attribute.type == "integer" %}
    {% for choice in attribute.choices %}
    { id: {{ choice }}, name: {{ choice }} },
    {% endfor %}
    {% else %}
    {% for choice in attribute.choices %}
    { id: '{{ choice }}', name: '{{ choice }}' },
    {% endfor %}
    {% endif%}
];

{% endif %}
{% endfor %}
{% endif %}
{% if resource.edit %}
{% for attribute in resource.edit %}
{% if attribute.choices %}
const editchoice{{ attribute.source }} = [
    {% if attribute.type == "integer" %}
    {% for choice in attribute.choices %}
    { id: {{ choice }}, name: {{ choice }} },
    {% endfor %}
    {% else %}
    {% for choice in attribute.choices %}
    { id: '{{ choice }}', name: '{{ choice }}' },
    {% endfor %}
    {% endif%}
];

{% endif %}
{% endfor %}
{% endif %}
{% for component, attributes in resource.items() %}
{% if component in supported_components and attributes|length > 0 %}
export const {{ resource.title }}{{ component|title }} = props => (
    <{{ component|title }} {...props} title="{{ resource.title }} {{ component|title }}"{% if component == "list" and resource.filters %} filters={<{{ resource.title }}Filter />}{% endif %}>
        <{% if component == "list" %}Datagrid{% elif component == "show" %}SimpleShowLayout{% else %}SimpleForm validate={validation{{ component|title }}{{ name }}}{% endif %}>
            {% for attribute in attributes %}
            {% if attribute.related_component %}
            <{{ attribute.component }} label="{{ attribute.label }}" source="{{ attribute.source }}" reference="{{ attribute.reference }}" {% if "Field" in attribute.component %}linkType="show" {% endif %}allowEmpty>
                <{{ attribute.related_component }} source="id" />
            </{{ attribute.component }}>
            {% else %}
            <{{ attribute.component }} source="{{ attribute.source }}" />
            {% endif %}
            {% endfor %}
            {% if component == "list" %}
            <EditButton />
            <ShowButton />
            <DeleteButton />
            {% endif %}
        </{% if component == "list" %}Datagrid{% elif component == "show" %}SimpleShowLayout{% else %}SimpleForm{% endif %}>
    </{{ component|title }}>
)

{% endif %}
{% endfor %}
/** End of Generated Code **/
