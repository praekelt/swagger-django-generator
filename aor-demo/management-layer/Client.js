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
    BooleanField,
    NumberField,
    DisabledInput,
    EditButton

} from 'admin-on-rest';

export const ClientList = props => (
    <List {...props} title="Client List">
        <Datagrid>
            <TextField source="client_id" />
            <BooleanField source="reuse_consent" />
            <TextField source="_redirect_uris" />
            <TextField source="logo" />
            <BooleanField source="require_consent" />
            <TextField source="terms_url" />
            <TextField source="_post_logout_redirect_uris" />
            <TextField source="name" />
            <TextField source="website_url" />
            <NumberField source="id" />
            <TextField source="contact_email" />
            <TextField source="response_type" />
        </Datagrid>
    </List>
)

export const ClientShow = props => (
    <Show {...props} title="Client Show">
        <SimpleShowLayout>
            <TextField source="client_id" />
            <BooleanField source="reuse_consent" />
            <TextField source="_redirect_uris" />
            <TextField source="logo" />
            <BooleanField source="require_consent" />
            <TextField source="terms_url" />
            <TextField source="_post_logout_redirect_uris" />
            <TextField source="name" />
            <TextField source="website_url" />
            <NumberField source="id" />
            <TextField source="contact_email" />
            <TextField source="response_type" />
        </SimpleShowLayout>
    </Show>
)

