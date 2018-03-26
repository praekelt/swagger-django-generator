import React from 'react';
import {
    List,
    Show,
    Edit,
    Create,
    Datagrid,
    SimpleShowLayout,
    SimpleForm,
    NumberField,
    TextField,
    TextInput,
    DisabledInput,
    DeleteButton,
    EditButton,
    ShowButton
} from 'admin-on-rest';

const validationCreateCategory = values => {
    const errors = {};
    if (!values.name) {
        errors.name = ["name is required"];
    }
    return errors;
}

export const CategoryList = props => (
    <List {...props} title="Category List">
        <Datagrid>
            <NumberField source="id" />
            <TextField source="name" />
            <EditButton />
            <ShowButton />
            <DeleteButton />
        </Datagrid>
    </List>
)

export const CategoryShow = props => (
    <Show {...props} title="Category Show">
        <SimpleShowLayout>
            <NumberField source="id" />
            <TextField source="name" />
        </SimpleShowLayout>
    </Show>
)

export const CategoryCreate = props => (
    <Create {...props} title="Category Create">
        <SimpleForm validate={validationCreateCategory}>
            <TextInput source="name" />
        </SimpleForm>
    </Create>
)

