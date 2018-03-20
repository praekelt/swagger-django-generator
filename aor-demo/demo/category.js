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

const validationCreatecategory = values => {
    const errors = {};
    if (!values.name) {
        errors.name = ["name is required"];
    }
    return errors;
}

export const CategoryList = props => (
    <List {...props} title="category List">
        <Datagrid>
            <TextField source="name" />
            <NumberField source="id" />
        </Datagrid>
    </List>
)

export const CategoryShow = props => (
    <Show {...props} title="category Show">
        <SimpleShowLayout>
            <TextField source="name" />
            <NumberField source="id" />
        </SimpleShowLayout>
    </Show>
)

export const CategoryCreate = props => (
    <Create {...props} title="Create category">
        <SimpleForm validate={validationCreatecategory}>
            <TextInput source="name" />
        </SimpleForm>
    </Create>
)

