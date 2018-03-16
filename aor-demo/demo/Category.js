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

const validationCreateCategory = values => {
    const errors = {};
    if (!values.name) {
        errors.name = ["name is required"];
    }
    return errors;
}

export const CategoryList = props => (
    <List {...props} title={"Category List"}>
        <DataGrid>
            <TextField source="name" />
            <NumberField source="id" />
        </DataGrid>
    </List>
)

export const CategoryShow = props => (
    <Show {...props} title={"Category Show"}>
        <SimpleShowLayout>
            <TextField source="name" />
            <NumberField source="id" />
        </SimpleShowLayout>
    </Show>
)

export const CategoryCreate = props => (
    <Create {...props} title={"Create Category"}>
        <SimpleForm validate={validationCreateCategory}>
            <TextInput source="name" />
        </SimpleForm>
    </Create>
)

