import React from 'react';
import {
    List,
    Show,
    Edit,
    Create,
    Datagrid,
    SimpleShowLayout,
    SimpleForm,
    TextField,
    TextInput,
    DateField,
    DateInput,
    NumberField,
    NumberInput,
    DisabledInput,
    EditButton

} from 'admin-on-rest';

const validationCreateDomain = values => {
    const errors = {};
    if (!values.name) {
        errors.name = ["name is required"];
    }
    return errors;
}

const validationEditDomain = values => {
    const errors = {};
    return errors;
}

export const DomainList = props => (
    <List {...props} title="Domain List">
        <Datagrid>
            <TextField source="name" />
            <DateField source="updated_at" />
            <NumberField source="parent_id" />
            <NumberField source="id" />
            <TextField source="description" />
            <DateField source="created_at" />
            <EditButton />
        </Datagrid>
    </List>
)

export const DomainShow = props => (
    <Show {...props} title="Domain Show">
        <SimpleShowLayout>
            <TextField source="name" />
            <DateField source="updated_at" />
            <NumberField source="parent_id" />
            <NumberField source="id" />
            <TextField source="description" />
            <DateField source="created_at" />
            <EditButton />
        </SimpleShowLayout>
    </Show>
)

export const DomainCreate = props => (
    <Create {...props} title="Create Domain">
        <SimpleForm validate={validationCreateDomain}>
            <NumberInput source="parent_id" />
            <TextInput source="name" />
            <TextInput source="description" />
        </SimpleForm>
    </Create>
)

export const DomainEdit = props => (
    <Edit {...props} title="Edit Domain">
        <SimpleForm validate={validationEditDomain}>
            <NumberInput source="parent_id" />
            <TextInput source="name" />
            <TextInput source="description" />
        </SimpleForm>
    </Edit>
)

