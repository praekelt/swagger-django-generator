/**
 * Generated {{ resource.title }}.js code. Edit at own risk.
 * When regenerated the changes will be lost.
**/
import React from 'react';
import {
    {% for import in resource.imports %}
    {% if import != "DateTimeInput" %}
    {{ import }},
    {% endif %}
    {% endfor %}
    DisabledInput,
    DeleteButton,
    EditButton,
    ShowButton
} from 'admin-on-rest';
{% if "DateTimeInput" in resource.imports %}
import DateTimeInput from 'aor-datetime-input';
{% endif %}
{% if resource.filters %}
import {
    {{ resource.title }}Filter
} from './Filters';
{% endif %}

{% if resource.create %}
const validationCreate{{ name }} = values => {
    const errors = {};
    {% for attribute in resource.create.fields %}
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
    {% for attribute in resource.edit.fields %}
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
{% for attribute in resource.create.fields %}
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
{% if resource.editW %}
{% for attribute in resource.edit.fields %}
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
{% for component, entries in resource.items() %}
{% if component in supported_components and (entries.fields|length > 0 or entries.inlines) %}
export const {{ resource.title }}{{ component|title }} = props => (
    <{{ component|title }} {...props} title="{{ resource.title }} {{ component|title }}"{% if component == "list" and resource.filters %} filters={<{{ resource.title }}Filter />}{% endif %}>
        <{% if component == "list" %}Datagrid{% elif component == "show" %}SimpleShowLayout{% else %}SimpleForm validate={validation{{ component|title }}{{ name }}}{% endif %}>
            {% for attribute in entries.fields %}
            {% if attribute.related_component %}
            <{{ attribute.component }} label="{{ attribute.label }}" source="{{ attribute.source }}" reference="{{ attribute.reference }}" {% if "Field" in attribute.component %}linkType="show" {% endif %}allowEmpty>
                <{% if attribute.read_only %}DisabledInput{% else %}{{ attribute.related_component }}{% endif %} source={% if "Input" in attribute.related_component %}"{{ attribute.related_field }}" optionText="{% if attribute.option_text %}{{ attribute.option_text }}{% endif %}"{% else %}"{% if attribute.option_text %}{{ attribute.option_text }}{% else %}id{% endif %}"{% endif %} />
            </{{ attribute.component }}>
            {% else %}
            <{% if attribute.read_only %}DisabledInput{% else %}{{ attribute.component }}{% endif %} source="{{ attribute.source }}"{% if attribute.type == "object" and "Input" in attribute.component %} format={value => value instanceof Object ? JSON.stringify(value) : value} parse={v => { try { return JSON.parse(v); } catch (e) { return v; } }}{% endif %} />
            {% endif %}
            {% endfor %}
            {% for inline in entries.inlines %}
            <{{ inline.component }} label="{{ inline.label }}" reference="{{ inline.reference }}" target="{{ inline.target }}">
                <Datagrid>
                    {% for attribute in inline.fields %}
                    {% if attribute.related_component %}
                    <{{ attribute.component }} label="{{ attribute.label }}" source="{{ attribute.source }}" reference="{{ attribute.reference }}" {% if "Field" in attribute.component %}linkType="show" {% endif %}allowEmpty>
                        <{% if attribute.read_only %}DisabledInput{% else %}{{ attribute.related_component }}{% endif %} source={% if "Input" in attribute.related_component %}"{{ attribute.related_field }}" optionText="{% if attribute.option_text %}{{ attribute.option_text }}{% endif %}"{% else %}"{% if attribute.option_text %}{{ attribute.option_text }}{% else %}id{% endif %}"{% endif %} />
                    </{{ attribute.component }}>
                    {% else %}
                    <{% if attribute.read_only %}DisabledInput{% else %}{{ attribute.component }}{% endif %} source="{{ attribute.source }}"{% if attribute.type == "object" and "Input" in attribute.component %} format={value => value instanceof Object ? JSON.stringify(value) : value} parse={v => { try { return JSON.parse(v); } catch (e) { return v; } }}{% endif %} />
                    {% endif %}
                    {% endfor %}
                </Datagrid>
            </{{ inline.component }}>
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
