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

export const TagList = props => (
    <List {...props} title={"Tag List"}>
        <DataGrid>
            <NumberField source="id" />
            <TextField source="name" />
        </DataGrid>
    </List>
)

export const TagShow = props => (
    <Show {...props} title={"Tag Show"}>
        <SimpleShowLayout>
            <NumberField source="id" />
            <TextField source="name" />
        </SimpleShowLayout>
    </Show>
)

