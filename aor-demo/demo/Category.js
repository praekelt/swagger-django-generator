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
    TextField,
} from 'admin-on-rest';

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

