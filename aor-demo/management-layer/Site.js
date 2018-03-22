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
    BooleanField,
    BooleanInput,
    DateField,
    DateInput,
    NumberField,
    NumberInput,
    DisabledInput,
    EditButton

} from 'admin-on-rest';

const validationCreateSite = values => {
    const errors = {};
    if (!values.domain_id) {
        errors.domain_id = ["domain_id is required"];
    }
    if (!values.name) {
        errors.name = ["name is required"];
    }
    return errors;
}

const validationEditSite = values => {
    const errors = {};
    return errors;
}

export const SiteList = props => (
    <List {...props} title="Site List">
        <Datagrid>
            <TextField source="client_id" />
            <BooleanField source="is_active" />
            <TextField source="name" />
            <DateField source="updated_at" />
            <NumberField source="domain_id" />
            <NumberField source="id" />
            <TextField source="description" />
            <DateField source="created_at" />
            <EditButton />
        </Datagrid>
    </List>
)

export const SiteShow = props => (
    <Show {...props} title="Site Show">
        <SimpleShowLayout>
            <TextField source="client_id" />
            <BooleanField source="is_active" />
            <TextField source="name" />
            <DateField source="updated_at" />
            <NumberField source="domain_id" />
            <NumberField source="id" />
            <TextField source="description" />
            <DateField source="created_at" />
            <EditButton />
        </SimpleShowLayout>
    </Show>
)

export const SiteCreate = props => (
    <Create {...props} title="Create Site">
        <SimpleForm validate={validationCreateSite}>
            <TextInput source="client_id" />
            <NumberInput source="domain_id" />
            <TextInput source="name" />
            <TextInput source="description" />
            <BooleanInput source="is_active" />
        </SimpleForm>
    </Create>
)

export const SiteEdit = props => (
    <Edit {...props} title="Edit Site">
        <SimpleForm validate={validationEditSite}>
            <TextInput source="client_id" />
            <NumberInput source="domain_id" />
            <TextInput source="name" />
            <TextInput source="description" />
            <BooleanInput source="is_active" />
        </SimpleForm>
    </Edit>
)

