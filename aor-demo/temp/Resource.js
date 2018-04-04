/**
 * Generated Resource.js code. Edit at own risk.
 * When regenerated the changes will be lost.
**/
import React from 'react';
import {
    List,
    Datagrid,
    NumberField,
    TextField,
    DateField,
    SimpleForm,
    Create,
    TextInput,
    Show,
    SimpleShowLayout,
    Edit,
    DeleteButton,
    EditButton,
    ShowButton
} from 'admin-on-rest';
import {
    ResourceFilter
} from './Filters';

const validationCreateResource = values => {
    const errors = {};
    if (!values.urn) {
        errors.urn = ["urn is required"];
    }
    return errors;
}

const validationEditResource = values => {
    const errors = {};
    return errors;
}

export const ResourceList = props => (
    <List {...props} title="Resource List" filters={<ResourceFilter />}>
        <Datagrid>
            <NumberField source="id" />
            <TextField source="urn" />
            <TextField source="description" />
            <DateField source="created_at" />
            <DateField source="updated_at" />
            <EditButton />
            <ShowButton />
            <DeleteButton />
        </Datagrid>
    </List>
)

export const ResourceCreate = props => (
    <Create {...props} title="Resource Create">
        <SimpleForm validate={validationCreateResource}>
            <TextInput source="urn" />
            <TextInput source="description" />
        </SimpleForm>
    </Create>
)

export const ResourceShow = props => (
    <Show {...props} title="Resource Show">
        <SimpleShowLayout>
            <NumberField source="id" />
            <TextField source="urn" />
            <TextField source="description" />
            <DateField source="created_at" />
            <DateField source="updated_at" />
        </SimpleShowLayout>
    </Show>
)

export const ResourceEdit = props => (
    <Edit {...props} title="Resource Edit">
        <SimpleForm validate={validationEditResource}>
            <TextInput source="urn" />
            <TextInput source="description" />
        </SimpleForm>
    </Edit>
)

/** End of Generated Code **/