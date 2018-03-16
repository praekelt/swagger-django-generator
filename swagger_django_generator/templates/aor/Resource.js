import React from 'react';
import {
    List,
    Show,
    Edit,
    Create,
    DataGrid,
    SimpleShowLayout,
    SimpleForm{% if resource.list_show %}{% for import in resource.list_show.imports %},
    {{ import }}Field{% if resource.create or resource.edit %},
    {{ import }}Input{% if import == "ReferenceArray" %},
    SingleFieldList,
    ChipField,
    SelectArrayInput{% endif %}{% endif %}{% endfor %}{% endif %},
    DisabledInput,
    EditButton

} from 'admin-on-rest';

{% if resource.create %}
const validationCreate{{ name }} = values => {
    const errors = {};
    {% for attribute in resource.create.attributes %}
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
    {% for attribute in resource.edit.attributes %}
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
{% for attribute in resource.create.attributes %}
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
{% for attribute in resource.edit.attributes %}
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
{% if resource.list_show %}
export const {{ resource.list_show.list_component }} = props => (
    <List {...props} title={"{{ name }} List"}>
        <DataGrid>
            {% for attribute in resource.list_show.attributes %}
            {% if attribute.type == "relation" %}
            <{{ attribute.component }}Field source="{{ attribute.source }}" reference="{{ attribute.reference }}">
                {% if attribute.component == "Reference" %}
                <TextField source="id" />
                {% elif attribute.component == "ReferenceArray" %}
                <SingleFieldList>
                    <ChipField source="id" />
                </SingleFieldList>
                {% endif %}
            </{{ attribute.component }}Field>
            {% else %}
            <{{ attribute.component }}Field source="{{ attribute.source }}" />
            {% endif %}
            {% endfor %}
            {% if resource.edit %}
            <EditButton />
            {% endif %}
        </DataGrid>
    </List>
)

export const {{ resource.list_show.show_component }} = props => (
    <Show {...props} title={"{{ name }} Show"}>
        <SimpleShowLayout>
            {% for attribute in resource.list_show.attributes %}
            {% if attribute.type == "relation" %}
            <{{ attribute.component }}Field source="{{ attribute.source }}" reference="{{ attribute.reference }}">
                {% if attribute.component == "Reference" %}
                <TextField source="id" />
                {% elif attribute.component == "ReferenceArray" %}
                <SingleFieldList>
                    <ChipField source="id" />
                </SingleFieldList>
                {% endif %}
            </{{ attribute.component }}Field>
            {% else %}
            <{{ attribute.component }}Field source="{{ attribute.source }}" />
            {% endif %}
            {% endfor %}
            {% if resource.edit %}
            <EditButton />
            {% endif %}
        </SimpleShowLayout>
    </Show>
)

{% endif %}
{% if resource.create %}
export const {{ resource.create.component }} = props => (
    <Create {...props} title={"Create {{ name }}"}>
        <SimpleForm validate={validationCreate{{ name }}}>
            {% for attribute in resource.create.attributes %}
            {% if attribute.type == "relation" %}
            <{{ attribute.component }}Input source="{{ attribute.source }}" reference="{{ attribute.reference }}">
                {% if attribute.component == "Reference" %}
                <SelectInput source="id" />
                {% elif attribute.component == "ReferenceArray" %}
                <SelectArrayInput optionText="id" />
                {% endif %}
            </{{ attribute.component }}Input>
            {% else %}
            <{{ attribute.component }}Input source="{{ attribute.source }}"{% if attribute.choices %} choices={createchoice{{ attribute.source }}}{% endif %} />
            {% endif %}
            {% endfor %}
        </SimpleForm>
    </Create>
)

{% endif %}
{% if resource.edit %}
export const {{ resource.edit.component }} = props => (
    <Edit {...props} title={"Edit {{ name }}"}>
        <SimpleForm validate={validationEdit{{ name }}}>
            {% for attribute in resource.edit.attributes %}
            {% if attribute.type == "relation" %}
            <{{ attribute.component }}Input source="{{ attribute.source }}" reference="{{ attribute.reference }}">
                {% if attribute.component == "Reference" %}
                <SelectInput source="id" />
                {% elif attribute.component == "ReferenceArray" %}
                <SelectArrayInput optionText="id" />
                {% endif %}
            </{{ attribute.component }}Input>
            {% else %}
            <{% if attribute.readOnly %}DisabledInput{% else %}{{ attribute.component }}Input{% endif %} source="{{ attribute.source }}"{% if attribute.choices %} choices={editchoice{{ attribute.source }}}{% endif %} />
            {% endif %}
            {% endfor %}
        </SimpleForm>
    </Edit>
)

{% endif %}