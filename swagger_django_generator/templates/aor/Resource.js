import React from 'react';
import {
    List,
    Show,
    Edit,
    Create,
    DataGrid,
    SimpleShowLayout,
    SimpleForm{% if resource.list_show %}{% for import in resource.list_show.imports %},
    {{ import }}Field{% endfor %}
    {% endif %}
    {% if resource.create %}
    {% for import in resource.create.imports %},
    {{ import }}Input
    {% endfor %},
    DisabledInput
    {% elif resource.edit %}
    {% for import in resource.edit.imports %},
    {{ import }}Input
    {% endfor %},
    DisabledInput
    {% endif %},{% if resource.edit %}
    EditButton
    {% endif %}

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
{% if resource.list_show %}
export const {{ resource.list_show.list_component }} = props => (
    <List {...props} title={"{{ name }} List"}>
        <DataGrid>
            {% for attribute in resource.list_show.attributes %}
            <{{ attribute.component }}Field source="{{ attribute.source }}" />
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
            <{{ attribute.component }}Field source="{{ attribute.source }}" />
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
            <{{ attribute.component }}Input source="{{ attribute.source }}" />
            {% endfor %}
        </SimpleForm>
    </Create>
)

{% endif %}
{% if resource.edit %}
export const {{ resource.edit.component }} = props => (
    <Edit {...props} title={"Edit {{ name }}"}>
        <SimpleForm validate={validationEdit{{ name }}}>
            {% for attribute in resource.create.attributes %}
            <{% if attribute.readOnly %}DisabledInput{% else %}{{ attribute.component }}Input{% endif %} source="{{ attribute.source }}" />
            {% endfor %}
        </SimpleForm>
    </Edit>
)

{% endif %}