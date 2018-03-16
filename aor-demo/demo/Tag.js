import React from 'react';
import {
    List,
    Show,
    Edit,
    Create,
    DataGrid,
    SimpleShowLayout,
    SimpleForm,
    TextField,
    TextInput,
    NumberField,
    NumberInput,
    DisabledInput,
    EditButton

} from 'admin-on-rest';

const validationEditTag = values => {
    const errors = {};
    return errors;
}

export const TagList = props => (
    <List {...props} title={"Tag List"}>
        <DataGrid>
            <TextField source="name" />
            <NumberField source="id" />
            <EditButton />
        </DataGrid>
    </List>
)

export const TagShow = props => (
    <Show {...props} title={"Tag Show"}>
        <SimpleShowLayout>
            <TextField source="name" />
            <NumberField source="id" />
            <EditButton />
        </SimpleShowLayout>
    </Show>
)

export const TagEdit = props => (
    <Edit {...props} title={"Edit Tag"}>
        <SimpleForm validate={validationEditTag}>
            <TextInput source="name" />
        </SimpleForm>
    </Edit>
)

