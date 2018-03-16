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
    NumberField,
} from 'admin-on-rest';

export const UserList = props => (
    <List {...props} title={"User List"}>
        <DataGrid>
            <TextField source="firstName" />
            <NumberField source="userStatus" />
            <NumberField source="id" />
            <TextField source="email" />
            <TextField source="username" />
            <TextField source="phone" />
            <TextField source="password" />
            <TextField source="lastName" />
        </DataGrid>
    </List>
)

export const UserShow = props => (
    <Show {...props} title={"User Show"}>
        <SimpleShowLayout>
            <TextField source="firstName" />
            <NumberField source="userStatus" />
            <NumberField source="id" />
            <TextField source="email" />
            <TextField source="username" />
            <TextField source="phone" />
            <TextField source="password" />
            <TextField source="lastName" />
        </SimpleShowLayout>
    </Show>
)

