/**
 * Generated Invitation.js code. Edit at own risk.
 * When regenerated the changes will be lost.
**/
import React from 'react';
import {
    List,
    Datagrid,
    TextField,
    ReferenceField,
    DateField,
    SimpleForm,
    Create,
    ReferenceInput,
    SelectInput,
    TextInput,
    Show,
    SimpleShowLayout,
    ReferenceManyField,
    NumberField,
    Edit,
    DeleteButton,
    EditButton,
    ShowButton
} from 'admin-on-rest';
import DateTimeInput from 'aor-datetime-input';
import {
    InvitationFilter
} from './Filters';

const validationCreateInvitation = values => {
    const errors = {};
    if (!values.invitor_id) {
        errors.invitor_id = ["invitor_id is required"];
    }
    if (!values.first_name) {
        errors.first_name = ["first_name is required"];
    }
    if (!values.last_name) {
        errors.last_name = ["last_name is required"];
    }
    if (!values.email) {
        errors.email = ["email is required"];
    }
    return errors;
}

const validationEditInvitation = values => {
    const errors = {};
    return errors;
}

export const InvitationList = props => (
    <List {...props} title="Invitation List" filters={<InvitationFilter />}>
        <Datagrid>
            <TextField source="id" />
            <ReferenceField label="User" source="invitor_id" reference="users" linkType="show" allowEmpty>
                <TextField source="username" />
            </ReferenceField>
            <TextField source="first_name" />
            <TextField source="last_name" />
            <TextField source="email" />
            <DateField source="expires_at" />
            <DateField source="created_at" />
            <DateField source="updated_at" />
            <EditButton />
            <ShowButton />
            <DeleteButton />
        </Datagrid>
    </List>
)

export const InvitationCreate = props => (
    <Create {...props} title="Invitation Create">
        <SimpleForm validate={validationCreateInvitation}>
            <ReferenceInput label="User" source="invitor_id" reference="users" allowEmpty>
                <SelectInput source="id" optionText="username" />
            </ReferenceInput>
            <TextInput source="first_name" />
            <TextInput source="last_name" />
            <TextInput source="email" />
            <DateTimeInput source="expires_at" />
        </SimpleForm>
    </Create>
)

export const InvitationShow = props => (
    <Show {...props} title="Invitation Show">
        <SimpleShowLayout>
            <TextField source="id" />
            <ReferenceField label="User" source="invitor_id" reference="users" linkType="show" allowEmpty>
                <TextField source="username" />
            </ReferenceField>
            <TextField source="first_name" />
            <TextField source="last_name" />
            <TextField source="email" />
            <DateField source="expires_at" />
            <DateField source="created_at" />
            <DateField source="updated_at" />
            <ReferenceManyField label="Domain Roles" reference="invitationdomainroles" target="invitation_id">
                <Datagrid>
                    <ReferenceField label="Domain" source="domain_id" reference="domains" linkType="show" allowEmpty>
                        <NumberField source="name" />
                    </ReferenceField>
                    <ReferenceField label="Role" source="role_id" reference="roles" linkType="show" allowEmpty>
                        <NumberField source="label" />
                    </ReferenceField>
                    <DateField source="created_at" />
                    <DateField source="updated_at" />
                </Datagrid>
            </ReferenceManyField>
            <ReferenceManyField label="Site Roles" reference="invitationsiteroles" target="invitation_id">
                <Datagrid>
                    <ReferenceField label="Site" source="site_id" reference="sites" linkType="show" allowEmpty>
                        <NumberField source="name" />
                    </ReferenceField>
                    <ReferenceField label="Role" source="role_id" reference="roles" linkType="show" allowEmpty>
                        <NumberField source="label" />
                    </ReferenceField>
                    <DateField source="created_at" />
                    <DateField source="updated_at" />
                </Datagrid>
            </ReferenceManyField>
        </SimpleShowLayout>
    </Show>
)

export const InvitationEdit = props => (
    <Edit {...props} title="Invitation Edit">
        <SimpleForm validate={validationEditInvitation}>
            <TextInput source="first_name" />
            <TextInput source="last_name" />
            <TextInput source="email" />
            <DateTimeInput source="expires_at" />
            <ReferenceManyField label="Domain Roles" reference="invitationdomainroles" target="invitation_id">
                <Datagrid>
                    <ReferenceField label="Domain" source="domain_id" reference="domains" linkType="show" allowEmpty>
                        <NumberField source="name" />
                    </ReferenceField>
                    <ReferenceField label="Role" source="role_id" reference="roles" linkType="show" allowEmpty>
                        <NumberField source="label" />
                    </ReferenceField>
                    <DateField source="created_at" />
                    <DateField source="updated_at" />
                    <EditButton />
                </Datagrid>
            </ReferenceManyField>
            <ReferenceManyField label="Site Roles" reference="invitationsiteroles" target="invitation_id">
                <Datagrid>
                    <ReferenceField label="Site" source="site_id" reference="sites" linkType="show" allowEmpty>
                        <NumberField source="name" />
                    </ReferenceField>
                    <ReferenceField label="Role" source="role_id" reference="roles" linkType="show" allowEmpty>
                        <NumberField source="label" />
                    </ReferenceField>
                    <DateField source="created_at" />
                    <DateField source="updated_at" />
                    <EditButton />
                </Datagrid>
            </ReferenceManyField>
        </SimpleForm>
    </Edit>
)

/** End of Generated Code **/