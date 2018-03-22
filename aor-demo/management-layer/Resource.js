import React from 'react';
import {
    List,
    Show,
    Edit,
    Create,
    Datagrid,
    SimpleShowLayout,
    SimpleForm,
    DateField,
    DateInput,
    NumberField,
    NumberInput,
    TextField,
    TextInput,
    DisabledInput,
    EditButton

} from 'admin-on-rest';

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
    <List {...props} title="Resource List">
        <Datagrid>
            <DateField source="updated_at" />
            <NumberField source="id" />
            <TextField source="description" />
            <DateField source="created_at" />
            <TextField source="urn" />
            <EditButton />
        </Datagrid>
    </List>
)

export const ResourceShow = props => (
    <Show {...props} title="Resource Show">
        <SimpleShowLayout>
            <DateField source="updated_at" />
            <NumberField source="id" />
            <TextField source="description" />
            <DateField source="created_at" />
            <TextField source="urn" />
            <EditButton />
        </SimpleShowLayout>
    </Show>
)

export const ResourceCreate = props => (
    <Create {...props} title="Create Resource">
        <SimpleForm validate={validationCreateResource}>
            <TextInput source="urn" />
            <TextInput source="description" />
        </SimpleForm>
    </Create>
)

export const ResourceEdit = props => (
    <Edit {...props} title="Edit Resource">
        <SimpleForm validate={validationEditResource}>
            <TextInput source="urn" />
            <TextInput source="description" />
        </SimpleForm>
    </Edit>
)

