/* tslint:disable */
/* eslint-disable */
/**
 * QuicDoc
 * Software meant to save you time editing documents and allow you to spend more time bringing in customers
 *
 * The version of the OpenAPI document: 0.1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { exists, mapValues } from '../runtime';
import type { Invitation } from './Invitation';
import {
    InvitationFromJSON,
    InvitationFromJSONTyped,
    InvitationToJSON,
} from './Invitation';
import type { Membership } from './Membership';
import {
    MembershipFromJSON,
    MembershipFromJSONTyped,
    MembershipToJSON,
} from './Membership';
import type { Subscription } from './Subscription';
import {
    SubscriptionFromJSON,
    SubscriptionFromJSONTyped,
    SubscriptionToJSON,
} from './Subscription';

/**
 * 
 * @export
 * @interface PatchedTeam
 */
export interface PatchedTeam {
    /**
     * 
     * @type {number}
     * @memberof PatchedTeam
     */
    readonly id?: number;
    /**
     * 
     * @type {string}
     * @memberof PatchedTeam
     */
    name?: string;
    /**
     * 
     * @type {string}
     * @memberof PatchedTeam
     */
    slug?: string;
    /**
     * 
     * @type {Array<Membership>}
     * @memberof PatchedTeam
     */
    readonly members?: Array<Membership>;
    /**
     * 
     * @type {Array<Invitation>}
     * @memberof PatchedTeam
     */
    readonly invitations?: Array<Invitation>;
    /**
     * 
     * @type {string}
     * @memberof PatchedTeam
     */
    readonly dashboardUrl?: string;
    /**
     * 
     * @type {boolean}
     * @memberof PatchedTeam
     */
    readonly isAdmin?: boolean;
    /**
     * 
     * @type {Subscription}
     * @memberof PatchedTeam
     */
    readonly subscription?: Subscription;
    /**
     * 
     * @type {boolean}
     * @memberof PatchedTeam
     */
    readonly hasActiveSubscription?: boolean;
}

/**
 * Check if a given object implements the PatchedTeam interface.
 */
export function instanceOfPatchedTeam(value: object): boolean {
    let isInstance = true;

    return isInstance;
}

export function PatchedTeamFromJSON(json: any): PatchedTeam {
    return PatchedTeamFromJSONTyped(json, false);
}

export function PatchedTeamFromJSONTyped(json: any, ignoreDiscriminator: boolean): PatchedTeam {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'id': !exists(json, 'id') ? undefined : json['id'],
        'name': !exists(json, 'name') ? undefined : json['name'],
        'slug': !exists(json, 'slug') ? undefined : json['slug'],
        'members': !exists(json, 'members') ? undefined : ((json['members'] as Array<any>).map(MembershipFromJSON)),
        'invitations': !exists(json, 'invitations') ? undefined : ((json['invitations'] as Array<any>).map(InvitationFromJSON)),
        'dashboardUrl': !exists(json, 'dashboard_url') ? undefined : json['dashboard_url'],
        'isAdmin': !exists(json, 'is_admin') ? undefined : json['is_admin'],
        'subscription': !exists(json, 'subscription') ? undefined : SubscriptionFromJSON(json['subscription']),
        'hasActiveSubscription': !exists(json, 'has_active_subscription') ? undefined : json['has_active_subscription'],
    };
}

export function PatchedTeamToJSON(value?: PatchedTeam | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'name': value.name,
        'slug': value.slug,
    };
}

