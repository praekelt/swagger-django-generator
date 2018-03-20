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
    NumberField,
    NumberInput,
    DisabledInput,
    EditButton

} from 'admin-on-rest';

const validationEdittag = values => {
    const errors = {};
    return errors;
}

export const TagList = props => (
    <List {...props} title="tag List">
        <Datagrid>
            <TextField source="name" />
            <NumberField source="id" />
            <EditButton />
        </Datagrid>
    </List>
)

export const TagShow = props => (
    <Show {...props} title="tag Show">
        <SimpleShowLayout>
            <TextField source="name" />
            <NumberField source="id" />
            <EditButton />
        </SimpleShowLayout>
    </Show>
)

export const TagEdit = props => (
    <Edit {...props} title="Edit tag">
        <SimpleForm validate={validationEdittag}>
            <TextInput source="name" />
        </SimpleForm>
    </Edit>
)

