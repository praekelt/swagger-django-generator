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
    NumberField,
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
            <TextField source="name" />
            <NumberField source="id" />
            <EditButton />
            <ShowButton />
            <DeleteButton />
        </Datagrid>
    </List>
)

export const CategoryCreate = props => (
    <Create {...props} title="Category Create">
        <SimpleForm validate={validationCreateCategory}>
            <TextInput source="name" />
        </SimpleForm>
    </Create>
)

export const CategoryShow = props => (
    <Show {...props} title="Category Show">
        <SimpleShowLayout>
            <TextField source="name" />
            <NumberField source="id" />
        </SimpleShowLayout>
    </Show>
)

