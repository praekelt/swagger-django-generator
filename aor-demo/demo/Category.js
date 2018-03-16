import React from 'react';
import {
    List,
    Show,
    Edit,
    Create,
    DataGrid,
    SimpleShowLayout,
    SimpleForm,
    NumberField,
    NumberInput,
    TextField,
    TextInput,
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
            <NumberField source="id" />
            <TextField source="name" />
        </DataGrid>
    </List>
)

export const CategoryShow = props => (
    <Show {...props} title={"Category Show"}>
        <SimpleShowLayout>
            <NumberField source="id" />
            <TextField source="name" />
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

