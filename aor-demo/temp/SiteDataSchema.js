/**
 * Generated SiteDataSchema.js code. Edit at own risk.
 * When regenerated the changes will be lost.
**/
import React from 'react';
import {
    List,
    Datagrid,
    ReferenceField,
    NumberField,
    DateField,
    SimpleForm,
    Create,
    ReferenceInput,
    SelectInput,
    LongTextInput,
    Show,
    SimpleShowLayout,
    Edit,
    DeleteButton,
    EditButton,
    ShowButton
} from 'admin-on-rest';
import {
    ObjectField
} from './CustomFields';
import {
    SiteDataSchemaFilter
} from './Filters';

const validationCreateSiteDataSchema = values => {
    const errors = {};
    if (!values.site_id) {
        errors.site_id = ["site_id is required"];
    }
    if (!values.schema) {
        errors.schema = ["schema is required"];
    }
    return errors;
}

const validationEditSiteDataSchema = values => {
    const errors = {};
    return errors;
}

export const SiteDataSchemaList = props => (
    <List {...props} title="SiteDataSchema List" filters={<SiteDataSchemaFilter />}>
        <Datagrid>
            <ReferenceField label="Site" source="site_id" reference="sites" linkType="show" allowEmpty>
                <NumberField source="name" />
            </ReferenceField>
            <ObjectField source="schema" addLabel />
            <DateField source="created_at" />
            <DateField source="updated_at" />
            <EditButton />
            <ShowButton />
            <DeleteButton />
        </Datagrid>
    </List>
)

export const SiteDataSchemaCreate = props => (
    <Create {...props} title="SiteDataSchema Create">
        <SimpleForm validate={validationCreateSiteDataSchema}>
            <ReferenceInput label="Site" source="site_id" reference="sites" allowEmpty>
                <SelectInput source="id" optionText="name" />
            </ReferenceInput>
            <LongTextInput source="schema" format={value => value instanceof Object ? JSON.stringify(value) : value} parse={value => { try { return JSON.parse(value); } catch (e) { return value; } }} />
        </SimpleForm>
    </Create>
)

export const SiteDataSchemaShow = props => (
    <Show {...props} title="SiteDataSchema Show">
        <SimpleShowLayout>
            <ReferenceField label="Site" source="site_id" reference="sites" linkType="show" allowEmpty>
                <NumberField source="name" />
            </ReferenceField>
            <ObjectField source="schema" addLabel />
            <DateField source="created_at" />
            <DateField source="updated_at" />
        </SimpleShowLayout>
    </Show>
)

export const SiteDataSchemaEdit = props => (
    <Edit {...props} title="SiteDataSchema Edit">
        <SimpleForm validate={validationEditSiteDataSchema}>
            <LongTextInput source="schema" format={value => value instanceof Object ? JSON.stringify(value) : value} parse={value => { try { return JSON.parse(value); } catch (e) { return value; } }} />
        </SimpleForm>
    </Edit>
)

/** End of Generated Code **/