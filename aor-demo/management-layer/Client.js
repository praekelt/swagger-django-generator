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
    BooleanField,
    DisabledInput,
    DeleteButton,
    EditButton,
    ShowButton
} from 'admin-on-rest';

export const ClientList = props => (
    <List {...props} title="Client List">
        <Datagrid>
            <TextField source="_post_logout_redirect_uris" />
            <NumberField source="id" />
            <TextField source="_redirect_uris" />
            <ReferenceField label="Client" source="client_id" reference="clients" allowEmpty>
                <TextField source="id" />
            </ReferenceField>
            <TextField source="terms_url" />
            <TextField source="response_type" />
            <TextField source="contact_email" />
            <TextField source="name" />
            <BooleanField source="reuse_consent" />
            <BooleanField source="require_consent" />
            <TextField source="logo" />
            <TextField source="website_url" />
            <EditButton />
            <ShowButton />
            <DeleteButton />
        </Datagrid>
    </List>
)

export const ClientShow = props => (
    <Show {...props} title="Client Show">
        <SimpleShowLayout>
            <TextField source="_post_logout_redirect_uris" />
            <NumberField source="id" />
            <TextField source="_redirect_uris" />
            <ReferenceField label="Client" source="client_id" reference="clients" allowEmpty>
                <TextField source="id" />
            </ReferenceField>
            <TextField source="terms_url" />
            <TextField source="response_type" />
            <TextField source="contact_email" />
            <TextField source="name" />
            <BooleanField source="reuse_consent" />
            <BooleanField source="require_consent" />
            <TextField source="logo" />
            <TextField source="website_url" />
        </SimpleShowLayout>
    </Show>
)

